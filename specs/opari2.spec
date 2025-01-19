Name:           opari2
Version:        2.0.8
Release:        3%{?dist}
Summary:        An OpenMP runtime performance measurement instrumenter

License:        BSD-3-Clause
URL:            https://www.vi-hps.org/projects/score-p/
Source0:        http://perftools.pages.jsc.fz-juelich.de/cicd/opari2/tags/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran

%description
OPARI2 is a source-to-source instrumentation tool for OpenMP and hybrid
codes.  It surrounds OpenMP directives and runtime library calls with calls
to the POMP2 measurement interface.

OPARI2 will provide you with a new initialization method that allows for
multi-directory and parallel builds as well as the usage of pre-instrumented
libraries. Furthermore, an efficient way of tracking parent-child
relationships was added. Additionally, we extended OPARI2 to support
instrumentation of OpenMP 3.0 tied tasks.


%prep
%autosetup -p1


%build
# I don't immediately see why using %%configure broke the check target
# in 2.0.7, which worked before.
./configure --disable-silent-rules --with-platform=linux --prefix=%_prefix \
            CFLAGS="%build_cflags" CXXFLAGS="%build_cxxflags" \
            LDFLAGS="%build_ldflags" FCFLAGS="%build_fcflags"
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete -print
find %{buildroot}%{_defaultdocdir}/%{name}/example* -name '*.a' -delete -print
# Avoid duplicated filelist with %%doc
cp -p AUTHORS ChangeLog README %{buildroot}%{_defaultdocdir}/%{name}/


%check
make check || ( cat */test-suite.log && exit 1 )


%files
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_libexecdir}/pomp2-parse-init-regions.awk
%{_includedir}/%{name}/
%{_defaultdocdir}/%{name}/
%{_datadir}/%{name}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Jan André Reuter <j.reuter@fz-juelich.de> - 2.0.8-1
- Update to 2.0.8

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Dave Love <loveshack@fedoraproject.org> - 2.0.7-1
- New version
- New download location

* Thu Sep  8 2022 Dave Love <loveshack@fedoraproject.org> - 2.0.6-5
- Use SPDX licence TAG

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Apr 13 2021 Dave Love <loveshack@fedoraproject.org> - 2.0.6-1
- New version
- Update source URL

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Dave love <loveshack@fedoraproject.org> - 2.0.5-1
- New version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Orion Poplawski <orion@nwra.com> - 2.0.4-1
- Update to 2.0.4

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-3
- Add patch to fix bad string access (FTBFS bug #1605309)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Orion Poplawski <orion@cora.nwra.com> - 2.0.3-1
- Update to 2.0.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Orion Poplawski <orion@cora.nwra.com> - 2.0.2-1
- Update to 2.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 7 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-3
- Add upstream patch to fix ppc64 builds

* Fri Nov 4 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-2
- Add BR gcc-c++
- Output test logs if they fail

* Tue Sep 20 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0.1-1
- Update to 2.0.1

* Fri Apr 15 2016 Orion Poplawski <orion@cora.nwra.com> - 2.0-1
- Update to 2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.4-7
- Update to 1.1.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 8 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.3-1
- Update to 1.1.3

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.2-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-3
- Add %%check
- Disable silent build

* Wed Feb 26 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-2
- Spec cleanup

* Wed Feb 26 2014 Orion Poplawski <orion@cora.nwra.com> - 1.1.2-1
- Update to 1.1.2

* Sun Oct 6 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-2
- Drop -devel sub-package
- New summary

* Wed Sep 25 2013 Orion Poplawski <orion@cora.nwra.com> - 1.1.1-1
- Update to 1.1.1

* Mon Apr 15 2013 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-2
- Add patch to put awk script into libexecdir

* Wed Apr 3 2013 Orion Poplawski <orion@cora.nwra.com> - 1.0.7-1
- Initial package
