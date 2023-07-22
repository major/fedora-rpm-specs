%global forgeurl https://github.com/troglobit/%{name}

Name:           libuev
Version:        2.4.0

%forgemeta

Release:        5%{?dist}
Summary:        Simple event loop for Linux
License:        MIT
URL:     %{forgeurl}
Source0: %{forgesource}

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make

%description
libuEv is a small event loop that wraps the Linux epoll() family
of APIs. It is similar to the more established libevent, libev 
and the venerable Xt(3) event loop. The µ in the name refers to 
both its limited feature set and the size impact of the library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for
developing application that use %{name}.

%prep
%setup -q
./autogen.sh

%build
%configure --disable-static
%make_build

%check
make check

%install
%make_install

# examples directory: remove unuseful files
find examples -type f \( -name "Makefile*" -or -name ".gitignore" \) -exec rm -f {} ';'

# remove docs from buildroot
rm -rf %{buildroot}%{_docdir}/libuev

# remove something unnecessary
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%license LICENSE
%doc README.md AUTHORS LICENSE ChangeLog.md
%{_libdir}/%{name}.so.3*

%files devel
%doc examples
%{_includedir}/uev
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 03 2021 Alessio <alessio@fedoraproject.org> - 2.4.0-1
- New release

* Mon Aug 02 2021 Alessio <alessio@fedoraproject.org> - 2.3.2-4
- https://github.com/troglobit/libuev/issues/25

* Sun Aug 01 2021 Alessio <alessio@fedoraproject.org> - 2.3.2-3
- Added _FILE_OFFSET_BITS=64 CPP flag BZ#1987665

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 31 2021 Alessio <alessio@fedoraproject.org> - 2.3.2-1
- Initial RPM version
