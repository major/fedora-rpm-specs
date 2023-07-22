%global svn_release 475

Name:           libcuefile
Version:        0
Release:        0.3.20110810svn%{svn_release}%{?dist}
Summary:        CUE file library from Musepack

License:        GPL-2.0-only WITH Bison-exception-2.2
URL:            https://www.musepack.net/index.php
Source0:        http://files.musepack.net/source/%{name}_r%{svn_release}.tar.gz
Patch99:	libcuefile-fedora-c99.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  sed

%description
CUE file library used by Musepack utilities and libraries


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}_r%{svn_release}
%patch 99 -p1

# Correct permissions and end of line
find -type f -exec chmod 0644 '{}' +
sed -ibackup 's/\r$//' CMakeLists.txt


%build
%cmake .
%cmake_build


%install
%cmake_install
# Remove static lib
rm %{buildroot}%{_libdir}/%{name}.a

install -D -t %{buildroot}%{_includedir}/cuetools/ include/cuetools/*.h


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/libcuefile.so.0{,.*}

%files devel
%{_includedir}/cuetools/
%{_libdir}/libcuefile.so


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20110810svn475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 DJ Delorie <dj@redhat.com> - 0-0.2.20110810svn475
- Fix C99 compatibility issue

%autochangelog
