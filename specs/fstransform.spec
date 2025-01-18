# help2man is too old on rhel <= 6 to support some switches.
%if 0%{?fedora} || 0%{?rhel} >= 7
%bcond_without	man
%else
%bcond_with	man
%endif


Name:		fstransform
Version:	0.9.4
Release:	16%{?dist}
Summary:	Tool for in-place file-system conversion without backup

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/cosmos72/%{name}
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	e2fsprogs-devel
BuildRequires:	gcc-c++
BuildRequires:	libcom_err-devel
BuildRequires:	zlib-devel

%if %{with man}
BuildRequires:	help2man
%endif # with man
BuildRequires: make

Requires:	coreutils
Requires:	util-linux
Requires:	which

%description
fstransform is a tool to change a file-system from one format
to another, for example from jfs/xfs/reiser to ext2/ext3/ext4,
in-place and without the need for backup.


%prep
%autosetup -p 1

# Make sure Autotools files have proper timestamps.
/bin/touch aclocal.m4 configure Makefile.am Makefile.in


%build
%configure --disable-silent-rules
%make_build


%install
%make_install

%if %{with man}
# Create man-pages.
%{__mkdir} -p %{buildroot}%{_mandir}/man8
for f in %{buildroot}%{_sbindir}/* ; do
	n="$(echo ${f} | %{__sed} -e 's!^%{buildroot}%{_sbindir}/!!g')"
	%{_bindir}/help2man -N -s 8 --version-string='%{version}'	\
		--no-discard-stderr -o %{buildroot}%{_mandir}/man8/${n}.8 ${f}
done
%endif # with man


%check
%make_build check


%files
%doc doc/*
%doc ChangeLog
%doc README
%doc TODO
%license AUTHORS
%license COPYING
%if %{with man}
%{_mandir}/man8/fsattr.8*
%{_mandir}/man8/fsmount_kernel.8*
%{_mandir}/man8/fsmove.8*
%{_mandir}/man8/fsremap.8*
%{_mandir}/man8/%{name}.8*
%endif # with man
%{_sbindir}/fsattr
%{_sbindir}/fsmount_kernel
%{_sbindir}/fsmove
%{_sbindir}/fsremap
%{_sbindir}/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.4-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.4-2
- Add some BuildRequires to enable optional functionality

* Wed May 08 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.4-1
- New upstream release

* Wed May 08 2019 Björn Esser <besser82@fedoraproject.org> - 0.9.3-5
- Add upstream patch fixing data loss bug (#1705564)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.3-1
- Initial import (rhbz#1484166)

* Tue Aug 22 2017 Björn Esser <besser82@fedoraproject.org> - 0.9.3-0.1
- Initial rpm release (rhbz#1484166)
