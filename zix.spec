%global         forgeurl https://gitlab.com/drobilla/zix
%global         commit 262d4a1522c38be0588746e874159da5c7bb457d

%global         maj 0

%forgemeta

Name:           zix
Version:        0.3.1
Release:        7%{?dist}
Summary:        A lightweight C library of portability wrappers and data structures

License:        ISC
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxygen

%description
%{name} is a lightweight C library of portability wrappers and data structures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Provides:       bundled(js-jquery) = 3.6.0
Buildarch:      noarch

%description    doc
The %{name}-doc package contains documentation files for
developing applications that use %{name}.

%prep
%forgesetup

%build
# Do not build benchmarks
%meson -Dbenchmarks=disabled
%meson_build

%install
%meson_install
# Delete duplicated sphinx docs
rm -rf %{buildroot}%{_docdir}/%{name}-%{maj}/singlehtml
# Delete sphinx buildinfo
rm -f %{buildroot}%{_docdir}/%{name}-%{maj}/html/.buildinfo
# Move devel docs to the right directory
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_libdir}/lib%{name}-%{maj}.so.%{maj}*

%files devel
%{_includedir}/%{name}-%{maj}
%{_libdir}/lib%{name}-%{maj}.so
%{_libdir}/pkgconfig/%{name}-%{maj}.pc

%files doc
%license COPYING
%doc %{_docdir}/%{name}/%{name}-%{maj}

%changelog
* Sat Aug 12 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-7
- Drop dependency from doc package

* Sun Apr 16 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-6
- Delete single html documetation
- Make doc package noarch

* Sun Mar 19 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-5
- Put documentation files into separate package

* Sat Mar 11 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-4
- Fix BRs

* Sun Feb 26 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-3
- Enable docs

* Sun Feb 05 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-2
- Remove unneeded BR glib2-devel

* Sun Feb 05 2023 Guido Aulisi <guido.aulisi@gmail.com> - 0.3.1-1
- Initial import
