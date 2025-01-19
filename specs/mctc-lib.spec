Name:           mctc-lib
Version:        0.3.2
Release:        2%{?dist}
Summary:        Modular computation tool chain library
License:        Apache-2.0
URL:            https://grimme-lab.github.io/mctc-lib/
Source0:        https://github.com/grimme-lab/mctc-lib/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  gcc-gfortran
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  json-fortran-devel
# For docs
BuildRequires:  rubygem-asciidoctor

# Patch to use python3 instead of env python3
Patch0:         mctc-lib-0.3.2-python3.patch

%description
Common tool chain for working with molecular structure data in various
applications. This library provides a unified way to perform
operations on molecular structure data, like reading and writing to
common geometry file formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch -P0 -p1 -b .python3

%build
export FFLAGS="%{optflags} -I%{_fmoddir} -fPIC"
export FCLAGS="%{optflags} -I%{_fmoddir} -fPIC"
%meson
%meson_build

%install
%meson_install
# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

# Move module files
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/mctc-lib/*/*.mod %{buildroot}%{_fmoddir}
rm -rf %{buildroot}%{_includedir}/mctc-lib/

%files
%license LICENSE
%doc README.md
%{_bindir}/mctc-convert
%{_mandir}/man1/mctc-convert.1*
%{_libdir}/libmctc-lib*.so.0*

%files devel
%{_fmoddir}/mctc_*.mod
%{_libdir}/pkgconfig/mctc-lib.pc
%{_libdir}/libmctc-lib.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Sep 06 2024 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2.

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-3
- Use %%{_fmoddir} in spec.

* Thu Jun 09 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-2
- Fix build in mock.

* Tue May 24 2022 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.3.0-1
- Initial release.
