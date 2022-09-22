%global srcname satyr
%define satyr_ver 0.26-2

Name: python-%{srcname}
Version: 0.26
Release: 3%{?dist}
Summary: Python binding for satyr
License: GPLv2+
URL: https://github.com/abrt/%{srcname}
Source0: https://github.com/abrt/%{srcname}/releases/download/%{version}/%{srcname}-%{version}.tar.xz
BuildRequires: python3-devel
BuildRequires: elfutils-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: binutils-devel
BuildRequires: rpm-devel
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: gdb

# git is need for '%%autosetup -S git' which automatically applies all the
# patches above. Please, be aware that the patches must be generated
# by 'git format-patch'
BuildRequires: git-core

Patch0001: 0001-Anonymize-paths-in-frames.patch
Patch0002: 0002-testsuite-Correct-syntax-for-gdb-backtrace-command.patch

%description
Satyr is a library that can be used to create and process microreports.
Microreports consist of structured data suitable to be analyzed in a fully
automated manner, though they do not necessarily contain sufficient information
to fix the underlying problem. The reports are designed not to contain any
potentially sensitive data to eliminate the need for review before submission.
Included is a tool that can create microreports and perform some basic
operations on them.

%package -n python3-%{srcname}
Summary: Python 3 bindings for satyr
Requires: %{srcname} >= %{satyr_ver}

%description -n python3-%{srcname}
Python 3 bindings for %{name}.

%prep
%autosetup -S git -n %{srcname}-%{version}

%build
%configure \
        --without-python2 \
        --disable-static

%make_build

%install
%make_install

# Remove all libtool archives (*.la) from modules directory.
find %{buildroot} -name "*.la" | xargs rm --

%check
make check|| {
    # find and print the logs of failed test
    # do not cat tests/testsuite.log because it contains a lot of bloat
    find tests/testsuite.dir -name "testsuite.log" -print -exec cat '{}' \;
    exit 1
}

%files -n python3-%{srcname}
%doc README NEWS
%license COPYING
%dir %{python3_sitearch}/%{srcname}
%{python3_sitearch}/%{srcname}/*

%exclude %{_bindir}/%{srcname}
%exclude %{_mandir}/man1/%{srcname}.1*
%exclude %{_libdir}/lib*.so.*
%exclude %{_includedir}/*
%exclude %{_libdir}/lib*.so
%exclude %{_libdir}/pkgconfig/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Martin Kutlak <mkutlak@redhat.com> 0.26-2
- Anonymize paths in frames
- Test fix: correct syntax for gdb backtrace command
- Initial python-satyr commit for satyr 0.26
