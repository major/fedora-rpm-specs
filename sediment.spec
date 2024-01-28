Name:		sediment
Version:	0.9.1
Release:	15%{?dist}
Summary:	A function reordering tool set

License:	GPLv3+
URL:		https://github.com/wcohen/sediment
# rpmbuild doesn't like it, but actual GitHub URL is:
# https://github.com/wcohen/sediment/archive/%%{version}.tar.gz
Source0:	https://github.com/wcohen/sediment/archive/sediment-%{version}.tar.gz
Patch1:		sediment-directory.patch

# sphinx is used for building documentation:
BuildRequires: make
BuildRequires: python3-sphinx >= 2.0
BuildRequires: automake
BuildRequires: autoconf
#Requires: gcc-python3-plugin
Requires: python3dist(gv)
BuildArch: noarch

%description
The sediment tool set allows reordering of the functions in compiled
programs built with RPM to reduce the frequency of TLB misses and
decrease the number of pages in the resident set.  Sediment generates
call graphs from program execution and converts the call graphs into
link order information to improve code locality.

%prep
%setup -q
%patch1 -p1 -b .directory


%build
autoreconf -iv
%configure
# doc makefile using sphinx does not work with parallel build
make

%install
%make_install


%files
%{_bindir}/gv2link
%{_bindir}/perf2gv
%{_bindir}/gen_profile_merge
%{_libexecdir}/%{name}
%{_docdir}/sediment/html
%doc README AUTHORS NEWS COPYING
%{_mandir}/man1/*


%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-6
- Require Python 3 gv, not Python 2 gv

* Thu Aug 8 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Fix ftbfs rhbz#1736649

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 William Cohen <wcohen@redhat.com> - 0.9.1-2
- Rebase to sediment-0.9.1
- Use python3-sphinx to build documentation.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9-3
- Update graphviz dependency

* Wed Mar 07 2018 William Cohen <wcohen@redhat.com> - 0.9-2
- Add automake build requires.

* Wed Mar 07 2018 William Cohen <wcohen@redhat.com> - 0.9-1
- Rebuild on sediment 0.9.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-10
- Fix FTBFS issues.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 09 2016 William Cohen <wcohen@redhat.com> 0.8-7
- Correct shebang issue flagged by rpmlint.

* Fri Feb 05 2016 William Cohen <wcohen@redhat.com> 0.8-6
- Include doc files twice in newer Fedora distributions.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 William Cohen <wcohen@redhat.com> 0.8-2
- Avoid listing doc files twice in newer Fedora distributions.

* Wed Mar 05 2014 William Cohen <wcohen@redhat.com> 0.8-1
- Rebase on sediment-0.7.

* Mon Mar 03 2014 William Cohen <wcohen@redhat.com> 0.7-1
- Rebase on sediment-0.7.

* Fri Feb 28 2014 William Cohen <wcohen@redhat.com> 0.6-1
- Update package and spec file based on Fedora package review rhbz 1070449.

* Thu Feb 27 2014 William Cohen <wcohen@redhat.com> 0.5-2
- Update spec file based on Fedora package review rhbz 1070449.

* Wed Feb 26 2014 William Cohen <wcohen@redhat.com> 0.5-1
- Bump version.

* Wed Feb 26 2014 William Cohen <wcohen@redhat.com> 0.4-1
- Bump version.

* Wed Feb 26 2014 William Cohen <wcohen@redhat.com> 0.3-3
- Move write-dot-callgraph.py out of /usr/bin.

* Mon Feb 24 2014 William Cohen <wcohen@redhat.com> 0.3-2
- spec file fixes based on comments.

* Mon Feb 24 2014 William Cohen <wcohen@redhat.com> 0.3-1
- Bump version.

* Mon Feb 24 2014 William Cohen <wcohen@redhat.com> 0.2-3
- Add basic man pages for perf2gv.py and gv2link.py.

* Wed Feb 19 2014 William Cohen <wcohen@redhat.com> 0.2-1
- Bump version to 0.2.

* Tue Feb 18 2014 William Cohen <wcohen@redhat.com> 0.1-2
- Add graphviz-python requires.

* Thu Feb 14 2013 William Cohen <wcohen@redhat.com> 0.1-1
- Initial release
