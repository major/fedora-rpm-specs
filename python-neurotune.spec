# Because the tests compile NEURON mod files which are arch dependent, we make
# this package archful, but disable debuginfo
%global debug_package %{nil}

%global forgeurl https://github.com/NeuralEnsemble/neurotune/

%global tag v0.2.6

%global _description %{expand:
This package provides Neurotune, a package for optimizing electical models of
excitable cells.

This package was originally developed by Mike Vella. This has been updated by
Padraig Gleeson and others (and moved to NeuralEnsemble) to continue
development of pyelectro and Neurotune for use in OpenWorm, Open Source Brain
and other projects.}

Name:           python-neurotune
Version:        0.2.6
%forgemeta

Release:        %autorelease
Summary:        A package for optimizing electical models of excitable cells
# spdx
License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description %_description

%package -n python3-neurotune
Summary:        %{summary}
BuildRequires:  python3-devel
# Required for compiling neuron mod files
BuildRequires:  neuron-devel

%description -n python3-neurotune %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package provides documentation for %{name}.

%prep
%forgesetup

# do not use pip install
sed -i '/pip/ d' test.sh

# Make python versioned in test script
sed -i "s|python|%{python3}|" test.sh

# Do not pollute the examples folder with compiled bits because we want to package it
cp -rv examples/ examples-temp/
sed -i "s|examples|examples-temp|" test.sh

# use the Fedora package
sed -i "s/.*pyelectro.*/pyelectro/" requirements-dev.txt

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
# find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

# see pyproject-rpm-macros documentation for more forms
%generate_buildrequires
%pyproject_buildrequires -r requirements-dev.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l neurotune

%check
# remove src folder so that we use built version
rm -rf neurotune
%{py3_test_envvars} ./test.sh

%files -n python3-neurotune -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc examples

%changelog
%autochangelog
