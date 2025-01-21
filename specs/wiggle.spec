Name:           wiggle
Version:        1.3
Release:        4%{?dist}
Summary:        A tool for applying patches with conflicts

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://neil.brown.name/wiggle/
Source0:        http://neil.brown.name/wiggle/%{name}-%{version}.tar.gz
Patch0:         wiggle-fix-build.patch


BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  groff
BuildRequires:  time
BuildRequires:  ncurses-devel

# The source tarball used, is obtained by visiting the URL above and
# getting a snapshot that contains the latest sources.  This can be
# done by clicking the 'snapshot' link listed on the gitweb interface
# This snapshot was the latest commit on the 'master' branch.
# 
# RPM doesn't particularly like this link as a 'Source', so I'll paste
# is here for posterity:
#
# http://neil.brown.name/git?p=wiggle;a=snapshot;h=1c5bfa7ce4de088e3b942463bb11cdc553a92b97;sf=tgz
#

%description
Wiggle is a program for applying patches that 'patch' cannot apply due
to conflicting changes in the original.

Wiggle will always apply all changes in the patch to the original.  If
it cannot find a way to cleanly apply a patch, it inserts it in the
original in a manner similar to 'merge', and reports an unresolvable
conflict.

%prep
%setup -q
%patch -P0 -p1 -b .build

%build
export CFLAGS="$RPM_OPT_FLAGS"
%make_build

%check
make test

%install
%make_install

%files
%license COPYING
%doc ANNOUNCE TODO
/usr/bin/wiggle
%{_mandir}/man1/wiggle.1*


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.3-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 18 2024 Sérgio Basto <sergio@serjux.com> - 1.3-1
- Update wiggle to 1.3

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 John W. Linville <linville@redhat.com> - 1.2-1
- Update to version 1.2 from upstream

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 John W. Linville <linville@redhat.com> - 1.1-1
- Update to version 1.1 from upstream
- Remove conflicting wiggle-Fix-endian-checks.patch

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0-10
- Escape macros in %%changelog

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 John W. Linville <linville@redhat.com> - 1.0-7
- Apply fix for endian checks from Neil Brown <neilb@suse.de>

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb  4 2015 John W. Linville <linville@redhat.com> 1.0-3
- Use %%license instead of %%doc for file containing license information

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 John W. Linville <linville@redhat.com> 1.0-1
- Rebased to new version of wiggle, 1.0.
- Some housekeeping in the spec file...

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 26 2010 Andy Gospodarek <gospo@redhat.com> 0.8-1
- Rebased to new version of wiggle, 0.8.

* Mon Oct 19 2009 Andy Gospodarek <gospo@redhat.com> 0.6-7
- Updated location for wiggle sources and uploaded new source-file. [506812]
- Dropped first patch since it was now included.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6-4
- Autorebuild for GCC 4.3

* Tue Jan 15 2008 Andy Gospodarek <gospo@redhat.com> 0.6-3
- More suggested package cleanups and doc additions

* Mon Jan 14 2008 Andy Gospodarek <gospo@redhat.com> 0.6-2
- Makefile changes and spec-file cleanups

* Mon Jan 14 2008 Andy Gospodarek <gospo@redhat.com> 0.6-1
- Initial build various patches from around the web

