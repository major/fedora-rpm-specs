Name:           tarpm
Version:        0.4
Release:        %autorelease
Summary:        RPM metadata and payload utility
Group:          Development/Tools
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/dcantrell/tarpm
Source0:        https://github.com/dcantrell/tarpm/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  rpm-devel
BuildRequires:  libarchive-devel >= 3.3.3
BuildRequires:  json-c-devel
BuildRequires:  CUnit-devel
BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  openssl-devel
BuildRequires:  file-devel
BuildRequires:  python3-rpm
BuildRequires:  python3-pip
BuildRequires:  rpm-build

# Only Fedora and EPEL 9 carry the RPM for the rpmfluff Python module
# right now (27OCT2026).
%if 0%{?rhel} == 0 || 0%{?rhel} == 9
BuildRequires:  python3-rpmfluff
%else
# pip builds rpmfluff from its sdist in %%check
BuildRequires:  python3-setuptools
%endif

%description
tarpm is a command line utility to create or extract built RPM and SRPM files.
The usual way of creating an RPM or SRPM is to use rpmbuild(8).  The tarpm(1)
program can take a built RPM or SRPM file and extract its contents to a
subdirectory, in a manner similar to using tar(1) to unpack a tar file.  The
RPM metadata is written to JSON files and the payload is extracted to a
subdirectory.  You can also use tarpm(1) to create an RPM or SRPM using the
header metadata in JSON files and the payload subdirectory.  The program will
recalculate the necessary checksums and digests to ensure the resulting
package is usable by rpm(8).


%prep
%autosetup


%build
%meson
%meson_build


%check
# If we lack the rpmfluff RPM, install it with pip.  This requires
# network access in mock or Copr builds.
%if 0%{?rhel} && 0%{?rhel} != 9
%{python3} -m pip install --user rpmfluff
%endif

%meson_test


%install
%meson_install


%files
%doc AUTHORS.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md RELEASE.org TODO.org
%license COPYING COPYING.LIB LICENSE-2.0.txt LICENSE-BSD.txt
%{_bindir}/tarpm
%{_mandir}/man1/tarpm.1*


%changelog
%autochangelog
