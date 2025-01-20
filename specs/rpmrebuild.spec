Name:           rpmrebuild
Version:        2.20
Release:        3%{?dist}
Summary:        A tool to build rpm file from rpm database

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://rpmrebuild.sourceforge.net

Source0:        http://downloads.sourceforge.net/rpmrebuild/%{name}-%{version}.tar.gz


BuildArch:      noarch
BuildRequires:  make
Requires:       rpm >= 4.0, rpm-build, coreutils, util-linux

%description
A tool to build an RPM file from a package that has already been installed.

%prep
%setup -q -c 

%build
make %{?_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

%files
%doc AUTHORS Changelog LISEZ.MOI News README Todo rpmrebuild.lsm Version
%license COPYING COPYRIGHT
%dir %{_prefix}/lib/rpmrebuild/
%dir %{_prefix}/lib/rpmrebuild/plugins/
%dir %{_prefix}/lib/rpmrebuild/locale/
%dir %{_prefix}/lib/rpmrebuild/locale/fr_FR.UTF-8
%dir %{_prefix}/lib/rpmrebuild/locale/en
%dir %{_prefix}/lib/rpmrebuild/locale/fr_FR
%attr(0755,root,root) %{_prefix}/bin/rpmrebuild
%config(noreplace)    %{_prefix}/lib/rpmrebuild/optional_tags.cfg
%attr(0644,root,root) %{_prefix}/lib/rpmrebuild/Version
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/nodoc.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_parser.src
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_extract_tags.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/processing_func.src
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_rpmqf.src
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_buildroot.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/spec_func.src
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_lib.src
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/uniq.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/un_prelink.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/unset_tag.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/demo.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/set_tag.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/file2pacDep.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/demofiles.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_ghost.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/rpmrebuild_files.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/compat_digest.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/exclude_file.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/empty_section.sh
%attr(0755,root,root) %{_prefix}/lib/rpmrebuild/plugins/replacefile.sh
%{_prefix}/lib/rpmrebuild/plugins/set_tag.plug
%{_prefix}/lib/rpmrebuild/plugins/compat_digest.plug
%{_prefix}/lib/rpmrebuild/plugins/nodoc.plug
%{_prefix}/lib/rpmrebuild/plugins/demo.plug
%{_prefix}/lib/rpmrebuild/plugins/file2pacDep.plug
%{_prefix}/lib/rpmrebuild/plugins/uniq.plug
%{_prefix}/lib/rpmrebuild/plugins/demofiles.plug
%{_prefix}/lib/rpmrebuild/plugins/un_prelink.plug
%{_prefix}/lib/rpmrebuild/plugins/unset_tag.plug
%{_prefix}/lib/rpmrebuild/plugins/exclude_file.plug
%{_prefix}/lib/rpmrebuild/plugins/empty_section.plug
%{_prefix}/lib/rpmrebuild/plugins/replacefile.plug
%{_prefix}/lib/rpmrebuild/locale/en/rpmrebuild.lang
%{_prefix}/lib/rpmrebuild/locale/fr_FR.UTF-8/rpmrebuild.lang
%{_prefix}/lib/rpmrebuild/locale/fr_FR/rpmrebuild.lang

%doc %{_mandir}/man1/rpmrebuild.1*
%doc %{_mandir}/fr_FR/man1/rpmrebuild.1*
%doc %{_mandir}/fr_FR.UTF-8/man1/rpmrebuild.1*
%doc %{_mandir}/man1/rpmrebuild_plugins.1*
%doc %{_mandir}/fr_FR/man1/rpmrebuild_plugins.1*
%doc %{_mandir}/fr_FR.UTF-8/man1/rpmrebuild_plugins.1*
%doc %{_mandir}/man1/compat_digest.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/compat_digest.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/compat_digest.plug.1rrp*
%doc %{_mandir}/man1/demo.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/demo.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/demo.plug.1rrp*
%doc %{_mandir}/man1/file2pacDep.plug.1rrp*
%doc %{_mandir}/man1/demofiles.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/demofiles.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/demofiles.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/file2pacDep.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/file2pacDep.plug.1rrp*
%doc %{_mandir}/man1/nodoc.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/nodoc.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/nodoc.plug.1rrp*
%doc %{_mandir}/man1/set_tag.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/set_tag.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/set_tag.plug.1rrp*
%doc %{_mandir}/man1/un_prelink.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/un_prelink.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/un_prelink.plug.1rrp*
%doc %{_mandir}/man1/unset_tag.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/unset_tag.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/unset_tag.plug.1rrp*
%doc %{_mandir}/man1/uniq.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/uniq.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/uniq.plug.1rrp*
%doc %{_mandir}/man1/exclude_file.plug.1rrp*
%doc %{_mandir}/fr_FR/man1/exclude_file.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/exclude_file.plug.1rrp*
%doc %{_mandir}/fr_FR.UTF-8/man1/empty_section.plug.1rrp.gz
%doc %{_mandir}/fr_FR.UTF-8/man1/replacefile.plug.1rrp.gz
%doc %{_mandir}/fr_FR/man1/empty_section.plug.1rrp.gz
%doc %{_mandir}/fr_FR/man1/replacefile.plug.1rrp.gz
%doc %{_mandir}/man1/empty_section.plug.1rrp.gz
%doc %{_mandir}/man1/replacefile.plug.1rrp.gz


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Michal Josef Špaček <mspacek@redhat.com> - 2.20-2
- Mark license files as %license

* Mon Dec 30 2024 Edgar Hoch <edgar.hoch@ims.uni-stuttgart.de> - 2.20-1
- Latest package from upstream.

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.17-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Anderson Silva <ansilva@redhat.com> - 2.17-1
- Latest package from upstream.

* Tue Aug 24 2021 Anderson Silva <ansilva@redhat.com> - 2.16-1
- Latest package from upstream.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 22 2020 Anderson Silva <ansilva@redhat.com> - 2.15.1
- Latest package from upstream.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.11-8
- Remove old crufty coreutils requires

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 09 2015 Anderson Silva <ansilva@redhat.com> - 2.11-3
- Fix --version option. BZ 1031101 

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 09 2014 Anderson Silva <ansilva@redhat.com> - 2.11-1
- New package from upstream.

* Sun Jan 20 2013 Anderson Silva <ansilva@redhat.com> - 2.9-1
- New package from upstream includes fix for Fedora 18.

* Fri Aug 10 2012 Anderson Silva <ansilva@redhat.com> - 2.8-1
- New package from upstream includes 2.7 version.

* Sun Nov 06 2011 Anderson Silva <ansilva@redhat.com> - 2.6-1
- New package from upstream.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Anderson Silva <ansilva@redhat.com> 2.3-3
- on F11 rpmrebuild requires rpm-build to be downloaded (live image at least)
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Jan 09 2009 Anderson Silva <ansilva@redhat.com> 2.3-1
- Introduces some fixes for compatibility with rpm 4.6.0 
* Thu Dec 04 2008 Anderson Silva <ansilva@redhat.com> 2.2.2-2
- Fix package ownership of locale directories.
* Sun May 11 2008 Anderson Silva <ansilva@redhat.com> 2.2.2-1
- New package from upstream.
- Removed dependency on rpm-rebuild, it is not available under EPEL.
* Fri Apr 04 2008 Anderson Silva <ansilva@redhat.com> 2.2.1-1
- New package from upstream.
- Fixed French man files to UTF8 into %%{_mandir}/fr/ directory
- Added some more basic dependencies
- Created a %%triggerin to allow rpmrebuild be used as a parameter for rpm
* Fri Sep 28 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-9
- Simpler %%postun provided by Mamoru Tasaka. Thanks.
* Fri Sep 28 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-8
- Replaced /usr/lib with %%{_prefix}/lib
- Fixed typo on popt.tmp filename
- fixed typo on %%changelog
- Added %%{_prefix}/lib/rpmbuild/plugins
* Thu Sep 27 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-7
- Changed /etc to %%{_sysconfdir}
- Fixed reference on postun section
- Using tarball as Source0
- Added require rpm-build
- Removed require for textutils, fileutils
- Added directories to belong to package
* Fri Sep 7 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-6
- Fixed error on sed script
- Upstream tarball comes from src.rpm (comment added)
* Wed Sep 5 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-5
- Optimized postun with sed
* Mon Aug 27 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-4
- Fixed Description once again
* Thu Aug 23 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-3
- Fixed Description
- Updated license
- Update %%doc
* Mon Aug 13 2007 Anderson Silva <ansilva@redhat.com> 2.1.1-2
- Assuming ownership of package.
* Thu Aug 09 2007 <smilner@redhat.com> 2.1.1-1
- Initial package following the Fedora packaging guidelines.
