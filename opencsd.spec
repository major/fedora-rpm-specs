%global opencsd_tag 691efce6ab357a35d16eb719498ca9aec72885d5

Name:           opencsd
Version:        1.3.3
Release:        0%{?dist}
Summary:        An open source CoreSight(tm) Trace Decode library

License:        BSD-3-Clause
URL:            https://github.com/Linaro/OpenCSD
Source0:        https://github.com/Linaro/OpenCSD/archive/%{opencsd_tag}.tar.gz

BuildRequires:  patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make

%description
This library provides an API suitable for the decode of ARM(r)
CoreSight(tm) trace streams.

%package devel
Summary: Development files for the CoreSight(tm) Trace Decode library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The opencsd-devel package contains headers and libraries needed
to develop CoreSight(tm) trace decoders.

%prep
%setup -q -n OpenCSD-%{opencsd_tag}

%build
cd decoder/build/linux
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
LIB_PATH=%{_lib} make %{?_smp_mflags}


%install
cd decoder/build/linux
PREFIX=%{buildroot}%{_prefix} LIB_PATH=%{_lib} make install DISABLE_STATIC=1 DEF_SO_PERM=755


%check
# no upstream unit tests yet

%files
%license LICENSE
%doc HOWTO.md README.md
%{_libdir}/*so\.*
%{_bindir}/*

%files devel
%doc decoder/docs/prog_guide/*
%{_includedir}/*
# no man files..
%{_libdir}/*so

#------------------------------------------------------------------------------
%changelog
* Wed Dec 14 2022 Jeremy Linton <jeremy.linton@arm.com> - 1.3.3-0
- Update to upstream 1.3.3, and SPDX migration

* Fri Oct 14 2022 Jeremy Linton <jeremy.linton@arm.com> - 1.3.2-1
- Update to upstream 1.3.2

* Thu Aug  4 2022 Jeremy Linton <jeremy.linton@arm.com> - 1.3.1-1
- Update to upstream 1.3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 24 2022 Jeremy Linton <jeremy.linton@arm.com> - 1.3.0-1
- Update to upstream 1.3.0

* Wed Jan 19 2022 Jeremy Linton <jeremy.linton@arm.com> - 1.2.0-1
- Update to upstream 1.2.0

* Fri Sep 10 2021 Jeremy Linton <jeremy.linton@arm.com> - 1.1.1-1
- Update to upstream 1.1.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 5 2021 Jeremy Linton <jeremy.linton@arm.com> - 1.0.0-1
- Update to upstream 1.0.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 23 2020 Jeremy Linton <jeremy.linton@arm.com> - 0.14.3-1
- Update to upstream 0.14.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Jeremy Linton <jeremy.linton@arm.com> - 0.14.1-1
- First opencsd package
