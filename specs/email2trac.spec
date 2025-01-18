# This spec file was derived from the upstream .spec file written by
# Jon Topper <jon at topper dot me dot uk>

# for now, Python3 support is on the main branch only
%global commit 0747a5a167ab236e86dcbd72f566457c4c28e29a
%global snapdate 20240910

Name:           email2trac
Version:        2.14.0^%{snapdate}git%{sub %{commit} 1 7}
Release:        2%{?dist}
Summary:        Utilities for converting emails to trac tickets
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://gitlab.com/surfsara/email2trac
# Source0:        https://mirror.ia.surf.nl/opensource/email2trac/email2trac-%%{version}.tar.gz
Source0:        https://gitlab.com/surfsara/email2trac/-/archive/%{commit}/email2trac-%{commit}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  make
Requires:       trac
Patch0:         email2trac-2.8.4-installperms.patch

%description
This is a release of the SARA package email2trac that contains
utilities that we use to convert emails to trac tickets. The initial
setup was made by Daniel Lundin from Edgewall Software. SARA has
extend the initial setup, with the following extensions:

 * HTML message conversion
 * Attachments
 * Tickets can be updated via email
 * Use command-line options
 * Configuration file to control the behavior.
 * Unicode support
 * SPAM detection
 * Workflow support
 * FullBlogPlugin support
 * DiscussionPlugin support


%prep
%autosetup -p1 -n email2trac-%{commit}


%build
export PYTHON=%{__python3}
%configure --with-trac_user=apache
%make_build


%install
make install DESTDIR=%{buildroot}


%files
%doc AUTHORS ChangeLog NOTICE README.md
%license LICENSE
%{_bindir}/delete_spam
%{_bindir}/email2trac
%{_bindir}/run_email2trac
%config(noreplace) %{_sysconfdir}/email2trac.conf


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0^20240910git0747a5a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Thomas Moschny <thomas.moschny@gmx.de> - 2.14.0^20240910git0747a5a-1
- Use git snapshot with Python3 support.

* Tue Oct 22 2024 Thomas Moschny <thomas.moschny@gmx.de> - 2.14.0-2
- Update URLs.

* Tue Oct 22 2024 Thomas Moschny <thomas.moschny@gmx.de> - 2.14.0-1
- Update to 2.14.0
- Use Python3.

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.2-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2.12.2-1
- Update to 2.12.2.
- Slightly modernize spec file.

* Sat Mar 24 2018 Thomas Moschny <thomas.moschny@gmx.de> - 2.11.0-4
- Add BR on gcc.

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.11.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug  9 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.11.0-1
- Update to 2.11.0.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.10.0-1
- Update to 2.10.0.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.9.0-1
- Update to 2.9.0.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.8-1
- Update to 2.8.8.

* Sat Apr 25 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.7-1
- Update to 2.8.7.
- Mark LICENSE with %%license.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.4-1
- Update to 2.8.4.
- Add patch applied upstream.

* Sat Apr 19 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.0-1
- Update to 2.8.0.
- Add patch to fix format-security error.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.0-1
- Updated to 2.7.0.

* Mon Mar 11 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.6.2-1
- Updated to 2.6.2.
  - License changed to ASL 2.0.
  - Updated URL.
  - Update one patch, drop obsolete patch.
- Modernize spec file.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 10 2009 Jesse Keating <jkeating@redhat.com> - 0.80-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Jesse Keating <jkeating@redhat.com> - 0.13-5
- Explicitly pass RPM_OPT_FLAGS

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 23 2008 Jesse Keating <jkeating@redhat.com> - 0.13-3
- Add a patch to handle both X-Spam-Score and X-Spam-Level

* Tue May 20 2008 Jesse Keating <jkeating@redhat.com> - 0.13-2
- BR python as per review.

* Mon May 19 2008 Jesse Keating <jkeating@redhat.com> - 0.13-1
- First submission to Fedora
