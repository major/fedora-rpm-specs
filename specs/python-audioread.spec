Summary:        Multi-library, cross-platform audio decoding in Python
Name:           python-audioread
Version:        3.0.1
Release:        6%{?dist}
License:        MIT
URL:            http://pypi.python.org/pypi/audioread/
Source0:        https://files.pythonhosted.org/packages/source/a/audioread/audioread-%{version}.tar.gz
Patch0:         0001-Remove-legacy-sound-modules-absent-in-Python-3.13.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  /usr/bin/ffmpeg
%global _description \
Decode audio files using whichever backend is available. Among\
currently supports backends are\
 o Gstreamer via PyGObject\
 o MAD via the pymad bindings\
 o FFmpeg or Libav via its command-line interface\
 o The standard library wave, aifc, and sunau modules
%description %_description

%package    -n  python3-audioread
Summary:        Multi-library, cross-platform audio decoding in Python
Requires:       python3-gobject
Requires:       (/usr/bin/ffmpeg or (gstreamer1 and gstreamer1-plugins-base and gstreamer1-plugins-good))
%{?python_provide:%python_provide python3-audioread}
%description -n python3-audioread %_description

%prep
%autosetup -p1 -n audioread-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-audioread
%doc README.rst decode.py
%{python3_sitelib}/audioread/
%{python3_sitelib}/audioread-*.dist-info/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 26 2024 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-5
- Remove legacy modules

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.0.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Terje Rosten <terje.rosten@ntnu.no> - 3.0.1-1
- 3.0.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 09 2023 Terje Rosten <terje.rosten@ntnu.no> - 3.0.0-4
- Remove use of imp module

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 27 2022 Terje Rosten <terje.rosten@ntnu.no> - 3.0.0-1
- 3.0.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.9-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Terje Rosten <terje.rosten@ntnu.no> - 2.1.9-1
- 2.1.9

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.8-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.1.8-3
- No Python 2 in newer Fedoras

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.8-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.1.8-1
- 2.1.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.1.7-1
- 2.1.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.6-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.1.6-1
- 2.1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.1.5-1
- 2.1.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-3
- Ranaming of pygobject3 was done in F23 (rhbz#1308613)

* Tue Feb 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-2
- Add proper python*-audioread provides

* Mon Feb 01 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-1
- 2.1.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 18 2013 Terje Røsten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1
- Python 3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Terje Røsten <terje.rosten@ntnu.no> - 0.6-1
- initial package

