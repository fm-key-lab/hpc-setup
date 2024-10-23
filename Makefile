# Usage: make GROUP_HOME=/path/to/group_home TASK_VERSION=3.39.2

CLONE := /usr/bin/git clone
TAR := /usr/bin/tar xf
WGET := /usr/bin/wget

MKDIR := mkdir -p
QUIET = @
RM := rm -f

CONFIG_FILE ?= $(CURDIR)/.env
GROUP_HOME ?= /nexus/posix0/MPIIB-keylab
TASK_EXE ?= ~/task
# If executable doesn't exist
VERSION ?= 3.39.2
PLATFORM ?= linux_amd64
TASK_URL := https://github.com/go-task/task/releases/download/v$(VERSION)/task_$(PLATFORM).tar.gz

GROUP_OPT := $(GROUP_HOME)/opt
GROUP_TOOLS := $(GROUP_HOME)/tools
GROUP_HOME_DIRS := $(GROUP_OPT) $(GROUP_TOOLS)

KEYLAB_GH := git@github.com:fm-key-lab
HPC_SETUP_REPO := $(KEYLAB_GH)/hpc-setup.git
SETUP_TOOLS := $(HPC_SETUP_REPO)

.PHONY: all clean

# Running the task executable from cwd will run Taskfile.yml
all: pre_deploy
	$(QUIET) $(TASK_EXE)

.PHONY: pre_deploy
pre_deploy: test_task_install setup_tools $(GROUP_HOME_DIRS) $(CONFIG_FILE)

.PHONY: lab_tools
setup_tools: $(GROUP_TOOLS)/hpc-setup

$(GROUP_TOOLS)/%:
	$(QUIET) cd $^ && \
	$(CLONE) $(KEYLAB_GH)/$*.git

.PHONY: test_task_install
test_task_install: $(TASK_EXE)
	$(QUIET) echo "$(shell $^ --version)"

$(TASK_EXE):
	$(QUIET) echo "Installing Taskfile to $^"
	$(QUIET) cd $^ && \
	$(WGET) $(TASK_URL) && \
	$(TAR) $(notdir $(TASK_URL)) && \
	$(RM) $(notdir $(TASK_URL))

$(GROUP_HOME_DIRS):
	$(QUIET) $(MKDIR) $@

$(CONFIG_FILE):
	$(QUIET) echo "Group home: $(GROUP_HOME)"
	$(QUIET) echo 'GROUP_HOME="$(GROUP_HOME)"' > $@

clean:
	$(QUIET) rm -rf $(GROUP_HOME_DIRS)
	$(QUIET) rm -f $(CONFIG_FILE)