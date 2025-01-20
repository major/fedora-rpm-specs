%global modname phyghtmap

Name:           python-phyghtmap
Version:        2.23
Release:        12%{?dist}
Summary:        Generate OSM contour lines from NASA SRTM data
License:        GPL-2.0-or-later
URL:            http://katze.tfiu.de/projects/phyghtmap/
Source0:        %{url}/%{modname}_%{version}.orig.tar.gz
# Compatibility fixes with newer numpy not yet upstream
Patch0:         0001-phyghtmap_numpy_arrays.patch
# Compatibility fixes for newer version of matplotplib, not yet upstream
Patch1:         0002-Fix_matplotlib_after_3_6_0.patch
BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
%{modname} is a little program which lets you easily generate OSM contour\
lines from NASA SRTM data.\


%description %_description

%package -n python3-phyghtmap
Summary: %summary
Requires:       python3-gdal
Requires:       python3-numpy
Requires:       python3-beautifulsoup4
Requires:       python3-matplotlib
# With matplotlib > 3.6.0, contour is used from external package
Requires:       python3-contourpy

%description -n python3-phyghtmap %_description

%prep
%autosetup -p 1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}
install -Dpm 644 docs/%{modname}.1 %{buildroot}%{_mandir}/man1/%{modname}.1


%files -n python3-%{modname} -f %{pyproject_files}
%doc README Changelog
%license LICENSE_GPL-2 COPYRIGHT
%{_bindir}/%{modname}
%{_mandir}/man1/%{modname}.1*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.23-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.23-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.23-4
- Drop support for i686

* Mon Nov 14 2022 Federico Pellegrin <fede@evolware.org> - 2.23-3
- Compatibility fixes for newer matplotlib > 3.6.0 (FC37 and future)

* Sun Nov 13 2022 Federico Pellegrin <fede@evolware.org> - 2.23-2
- Compatibility fixes with newer numpy array behaviour

* Mon Oct 31 2022 Federico Pellegrin <fede@evolware.org> - 2.23-1
- Bump to 2.23

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.21-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.21-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.21-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.21-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.21-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Miro Hrončok <mhroncok@redhat.com> - 2.21-1
- New upstream release
- Switch to Python 3

* Wed Aug 01 2018 Volker Fröhlich <volker27@gmx.at> - 2.20-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.10-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Dec 20 2017 Volker Fröhlich <volker27@gmx.at> - 2.10-1
- New upstream release

* Tue Sep 12 2017 Volker Fröhlich <volker27@gmx.at> - 2.0-1
- New upstream release

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.80-4
- Python 2 binary package renamed to python2-phyghtmap
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 07 2017 Volker Fröhlich <volker27@gmx.at> - 1.80-1
- New upstream release

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.74-4
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.74-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep  3 2015 Volker Fröhlich <volker27@gmx.at> - 1.74-1
- New upstream release

* Mon Aug 10 2015 Volker Fröhlich <volker27@gmx.at> - 1.73-1
- New upstream release

* Thu Jul 30 2015 Volker Fröhlich <volker27@gmx.at> - 1.72-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Volker Fröhlich <volker27@gmx.at> - 1.71-1
- New upstream release

* Tue May 26 2015 Volker Fröhlich <volker27@gmx.at> - 1.70-1
- New upstream release
- New functionality requires the gdal python bindings

* Mon Feb 23 2015 Volker Fröhlich <volker27@gmx.at> - 1.61-1
- New upstream release

* Sat Jan  3 2015 Volker Fröhlich <volker27@gmx.at> - 1.60-1
- New upstream release

* Mon Sep 29 2014 Volker Fröhlich <volker27@gmx.at> - 1.50-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Volker Fröhlich <volker27@gmx.at> - 1.49-1
- New upstream release

* Wed Mar 26 2014 Volker Fröhlich <volker27@gmx.at> - 1.48-1
- New upstream release

* Wed Oct  2 2013 Volker Fröhlich <volker27@gmx.at> - 1.47-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun  2 2013 Volker Fröhlich <volker27@gmx.at> - 1.45-2
- BR python2-devel instead of python-devel
- BR python-setuptools instead of ...-devel
- Change group to Applications/Engineering

* Sun May 26 2013 Volker Fröhlich <volker27@gmx.at> - 1.45-1
- Initial package for Fedora
