%global date 20121105
%global hash c55cb50
%global checkout %{date}git%{hash}
%global tarbase pmachata-dwlocstat-%{hash}

Name: dwlocstat
Version: 0.1
Release: 0.31.%{checkout}%{?dist}
Summary: Tool for examining Dwarf location info coverage

# The following files are dual-licensed:
#  dwarfstrings.h/.c, option.hh/.cc, iterators.hh
# The rest is GPLv3+ only.
# Automatically converted from old format: GPLv3+ and LGPLv3+ - review is highly recommended.
License: GPL-3.0-or-later AND LGPL-3.0-or-later
URL: https://github.com/pmachata/dwlocstat
# wget the following with --content-disposition
Source0: https://github.com/pmachata/dwlocstat/tarball/%{hash}/%{tarbase}.tar.gz
Patch0:  dwlocstat-remove-DW_TAG_mutable_type.patch
# 0.153 defines DW_OP_GNU_entry_value
BuildRequires:  gcc-c++
BuildRequires: elfutils-devel >= 0.153
BuildRequires: make

%description
dwlocstat is a tool for examining Dwarf location info coverage.  It
goes through DIEs of given binary's debug info that represent
variables and function parameters.  For each such DIE, it computes
coverage of that DIE's range by location expressions.

%prep
%setup -q -n %{tarbase}
%patch -P0 -p1

%build
make %{?_smp_mflags} dwlocstat \
     CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 -t $RPM_BUILD_ROOT%{_bindir} dwlocstat
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 -t $RPM_BUILD_ROOT%{_mandir}/man1 %{name}.1

%check
./dwlocstat ./dwlocstat

%files
%doc COPYING COPYING-LGPLV3 README
%{_bindir}/dwlocstat
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-0.30.20121105gitc55cb50
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.29.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.27.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.26.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.25.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.24.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.23.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.22.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.21.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.20.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.19.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.18.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.17.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.16.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.15.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.14.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.13.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.12.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.11.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.10.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1-0.8.20121105gitc55cb50
- Rebuilt for GCC 5 C++11 ABI change

* Fri Sep 05 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.1-0.7.20121105gitc55cb50
- remove DW_TAG_mutable_type as it was removed from DWARF spec

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.6.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.5.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.4.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.3.20121105gitc55cb50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov  5 2012 Petr Machata <pmachata@redhat.com> - 0.1-0.2.20121105gitc55cb50
- Clarify licensing
- Update to a new upstream, which unbundles several elfutils files

* Fri Oct 12 2012 Petr Machata <pmachata@redhat.com> - 0.1-0.1.20121012git4557c3e
- Initial packaging
