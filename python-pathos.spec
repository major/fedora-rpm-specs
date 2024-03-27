%global _description %{expand:
The pathos package provides a few basic tools to make parallel and distributed
computing more accessible to the end user. The goal of pathos is to enable the
user to extend their own code to parallel and distributed computing with
minimal refactoring.

pathos provides methods for configuring, launching, monitoring, and controlling
a service on a remote host. One of the most basic features of pathos is the
ability to configure and launch a RPC-based service on a remote host. pathos
seeds the remote host with the portpicker script, which allows the remote host
to inform the localhost of a port that is available for communication.

Beyond the ability to establish a RPC service, and then post requests, is the
ability to launch code in parallel. Unlike parallel computing performed at the
node level (typically with MPI), pathos enables the user to launch jobs in
parallel across heterogeneous distributed resources. pathos provides
distributed map and pipe algorithms, where a mix of local processors and
distributed workers can be selected. pathos also provides a very basic
automated load balancing service, as well as the ability for the user to
directly select the resources.

The high-level pool.map interface, yields a map implementation that hides the
RPC internals from the user. With pool.map, the user can launch their code in
parallel, and as a distributed service, using standard python and without
writing a line of server or parallel batch code.

RPC servers and communication in general is known to be insecure. However,
instead of attempting to make the RPC communication itself secure, pathos
provides the ability to automatically wrap any distributed service or
communication in a ssh-tunnel. Ssh is a universally trusted method. Using
ssh-tunnels, pathos has launched several distributed calculations on national
lab clusters, and to date has performed test calculations that utilize
node-to-node communication between several national lab clusters and a user's
laptop. pathos allows the user to configure and launch at a very atomic
level, through raw access to ssh and scp.

pathos is the core of a python framework for heterogeneous computing. pathos is
in active development, so any user feedback, bug reports, comments, or
suggestions are highly appreciated. A list of issues is located at
https://github.com/uqfoundation/pathos/issues, with a legacy list maintained at
https://uqfoundation.github.io/project/pathos/query.}

%global forgeurl https://github.com/uqfoundation/pathos/

Name:           python-pathos
Version:        0.3.2
Release:        %autorelease
Summary:        Parallel graph management and execution in heterogeneous computing

%global tag %{version}
%forgemeta

# SPDX
License:        BSD-3-Clause
URL:            %forgeurl
Source0:        %forgesource
BuildArch:      noarch

%description %_description

%package -n python3-pathos
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-pathos %_description

%package doc
Summary:        Documentation for %{name}

%description doc
This package includes examples for %{name}.

%prep
%forgesetup

# remove shebang
find . -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/d' '{}' \;

# Remove executable bit
chmod -x examples/*.py
chmod -x examples2/*.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
# Remove generated shebang from __info__.py (Kill it with fire!)
sed -i '/^#![  ]*\/usr\/bin\/env.*$/d' %{buildroot}%{python3_sitelib}/pathos/__info__.py
%pyproject_save_files -l pathos

%check
# Imitate tox.ini:
%{py3_test_envvars} %{python3} -m pathos.tests

%files -n python3-pathos -f %{pyproject_files}
%{_bindir}/portpicker
%{_bindir}/pathos_connect
%doc README.md

%files doc
%license LICENSE
%doc README.md
%doc examples/
%doc examples2/

%changelog
%autochangelog
