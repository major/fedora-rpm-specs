%undefine __cmake_in_source_build

Name:           tasksh
Version:        1.2.0
Release:        %autorelease
Summary:        Shell command that wraps Taskwarrior commands

# spdx
License:        MIT
URL:            https://taskwarrior.org/
Source0:        https://taskwarrior.org/download/%{name}-%{version}.tar.gz
# We install docs ourselves
Patch0:         0001-don-t-install-docs.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  readline-devel
Requires:       task

%description
Tasksh is a shell command that wraps Taskwarrior commands. It is intended to
provide simpler Taskwarrior access, and add a few new features of its own.

Tasksh replaces the built-in shell command of older releases, and the bundled
tasksh program of version 2.3.0. The former was very limited and the latter
unsupported, buggy and flawed.

%prep
%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381480)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc ChangeLog AUTHORS NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
