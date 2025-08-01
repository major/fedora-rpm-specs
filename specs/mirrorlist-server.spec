# Generated by rust2rpm 27
%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

Name:           mirrorlist-server
Version:        3.0.7
Release:        %autorelease
Summary:        Mirrorlist Server

SourceLicense:  MIT
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# ISC
# MIT
# MIT OR Apache-2.0
# Unicode-3.0
# Unlicense OR MIT
License:        %{shrink:
    MIT AND
    ISC AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    (Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/adrianreber/mirrorlist-server
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch:          0001-set-license-in-crate-metadata.patch
# https://github.com/adrianreber/mirrorlist-server/commit/4f59b4b
Patch:          0002-bump-pretty_env_logger-dependency-from-0.4-to-0.5.patch
# Allow console 0.16.0 and indicatif 0.18; see:
#
# Update console dependency to 0.16.0
# https://github.com/adrianreber/mirrorlist-server/pull/336
#
# Bump indicatif from 0.17.9 to 0.17.11
# https://github.com/adrianreber/mirrorlist-server/commit/da5c1b7070fe1ca2e5faffce62a2dcaf5f195fcf
Patch:          0003-Allow-console-0.16-and-indicatif-0.18.patch

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
The mirrorlist-server uses the data created by MirrorManager2
(https://github.com/fedora-infra/mirrormanager2) to answer client request for
the "best" mirror.

This implementation of the mirrorlist-server is written in Rust. The original
version of the mirrorlist-server was part of the MirrorManager2 repository and
it is implemented using Python. While moving from Python2 to Python3 one of
the problems was that the data exchange format (Python Pickle) did not support
running the MirrorManager2 backend with Python2 and the mirrorlist frontend
with Python3. To have a Pickle independent data exchange format protobuf was
introduced. The first try to use protobuf in the python mirrorlist
implementation required a lot more memory than the Pickle based implementation
(3.5GB instead of 1.1GB). That is one of the reasons a new mirrorlist-server
implementation was needed.

Another reason to rewrite the mirrorlist-server is its architecture. The
Python based version requires the Apache HTTP server or something that can
run the included wsgi. The wsgi talks over a socket to the actual
mirrorlist-server. In Fedora's MirrorManager2 instance this runs in a container
which runs behind HAProxy. This implementation in Rust directly uses a HTTP
library to reduce the number of involved components.

In addition to being simpler this implementation also requires less memory
than the Python version.}

%description %{_description}

%prep
%autosetup -n mirrorlist-server-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test -- --bin mirrorlist-server
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.rst
%{_bindir}/generate-mirrorlist-cache
%{_bindir}/mirrorlist-server

%changelog
%autochangelog
