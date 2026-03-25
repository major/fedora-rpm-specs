# do not produce empty debuginfo package
%global debug_package %{nil}
  
Summary: Dummy package for testing and on-boarding purposes
Name: redhat-internal-test-package
Version: 0.6.6
Release: %{autorelease}
License: GPL-2.0-or-later
URL: https://github.com/packit/redhat-internal-test-package
Group: Applications/File
Source0: https://github.com/packit/redhat-internal-test-package/archive/refs/tags/%{version}.tar.gz
Patch1: 0001-Change-hacker-to-haxxor.patch

BuildArch: noarch
BuildRequires: python3-devel

%description
Dummy package that is meant to be used for testing or on-boarding purposes,
but which should not ever get to a real release.

%prep
%autosetup -n redhat-internal-test-package-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires 

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files haxxor
install -D -m 644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.md
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/haxxor

%changelog
%autochangelog
