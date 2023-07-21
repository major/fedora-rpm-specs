%global sum Image Viewer and Toolkit
%global common_desc                                                           \
Ginga is a toolkit designed for building viewers for scientific image data in \
Python, visualizing 2D pixel data in numpy arrays. It can view astronomical   \
data such as contained in files based on the FITS (Flexible Image Transport   \
System) file format. It is written and is maintained by software engineers at \
the Subaru Telescope, National Astronomical Observatory of Japan.             \
                                                                              \
The Ginga toolkit centers around an image display class which supports zooming\
and panning, color and intensity mapping, a choice of several automatic cut   \
levels algorithms and canvases for plotting scalable geometric forms. In      \
addition to this widget, a general purpose “reference” FITS viewer is         \
provided, based on a plugin framework. A fairly complete set of standard      \
plugins are provided for features that we expect from a modern FITS viewer:   \
panning and zooming windows, star catalog access, cuts, star pick/fwhm,       \
thumbnails, etc.

Name:           ginga
Version:        4.0.1
Release:        4%{?dist}
Summary:        %{sum}
# License breakdown
#
# In general (if not listed below): BSD
#
# Apache 2.0
#   astropy_helpers/astropy_helpers/sphinx/themes/bootstrap-astropy/static/bootstrap-astropy.css
#   ginga/util/heaptimer.py
# 
# MIT/X11
#   ginga/util/six.py
#
License:        BSD and ASL 2.0 and MIT
URL:            https://ejeschke.github.io/ginga/
Source0:        https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz

# General build reqs
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
Requires:       python3-%{name} = %{version}-%{release}

BuildArch:      noarch

%description
%{common_desc}

%package -n python3-%{name}
Summary:        %{sum}
Requires:       google-roboto-fonts
Requires:       google-roboto-condensed-fonts

%description -n python3-%{name}
%{common_desc}

%package -n python3-%{name}-examples
Summary:        Examples for %{name}
Requires:       python3-%{name} = %{version}-%{release}

%description -n python3-%{name}-examples
Examples for %{name}

%pyproject_extras_subpkg -n python3-ginga recommended
%pyproject_extras_subpkg -n python3-ginga qt5

%prep
%autosetup
sed -i -e s/opencv-python/opencv/ -e s/python-magic.*/file-magic/ setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x recommended -x qt5

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ginga
sed -i '/Roboto.*LICENSE/d' %{pyproject_files}

desktop-file-install                                    \
     --dir=%{buildroot}%{_datadir}/applications         \
     %{name}.desktop

# Replace bundled fonts with symlinks to system fonts
rm %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto*/*
ln -sf %{_fontbasedir}/google-roboto/Roboto-Black.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Black.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Bold.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Bold.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Light.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Light.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Medium.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Medium.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Regular.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Regular.ttf
ln -sf %{_fontbasedir}/google-roboto/Roboto-Thin.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto/Roboto-Thin.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Bold.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Bold.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-BoldItalic.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-BoldItalic.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Light.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Light.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-LightItalic.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-LightItalic.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Italic.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Italic.ttf
ln -sf %{_fontbasedir}/google-roboto/RobotoCondensed-Regular.ttf %{buildroot}/%{python3_sitelib}/%{name}/fonts/Roboto_Condensed/RobotoCondensed-Regular.ttf
# TODO - Bundled Ubuntu_Mono

# ginga/web/pgw/ipg.py has wrong permissions
chmod 755 %{buildroot}/%{python3_sitelib}/%{name}/web/pgw/ipg.py
chmod 755 %{buildroot}/%{python3_sitelib}/%{name}/util/mosaic.py

# Fix wrong interpreters in some scripts...
%py3_shebang_fix %{buildroot}/%{python3_sitelib}/ginga/web/pgw/ipg.py %{buildroot}/%{python3_sitelib}/ginga/examples

%files
%doc README.md LONG_DESC.txt doc/WhatsNew.rst
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md
# Examples are shipped as documentation in examples subpackage
%exclude %{python3_sitelib}/%{name}/examples

%files -n python3-%{name}-examples
%doc ginga/examples

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Python Maint <python-maint@redhat.com> - 4.0.1-3
- Rebuilt for Python 3.12

* Fri Jul 07 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.1-2
- Rebuild for Python 3.12

* Sun Jun 25 2023 Orion Poplawski <orion@nwra.com> - 4.0.1-1
- Update to 4.0.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 2.7.2-13
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.7.2-10
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-6
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.7.2-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Christian Dersch <lupinix@mailbox.org> - 2.7.2-1
- new version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.7.1-2
- drop python2 subpackage (#1632317)

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.7.1-1
- new version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6.5-4
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.6.5-2
- Remove obsolete scriptlets

* Fri Sep 08 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.5-1
- new version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 18 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.2-2
- Added dependency python-QtPy

* Tue Feb 28 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.2-1
- new version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Christian Dersch <lupinix@mailbox.org> - 2.6.1-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6.0-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Christian Dersch <lupinix@mailbox.org> - 2.6.0-1
- new version

* Sat Oct 22 2016 Christian Dersch <lupinix@mailbox.org> - 2.5.20161005204600-1
- new version
- unbundled fonts
- fixed interpreters for scripts to use correct Python version

* Sun Oct  2 2016 Christian Dersch <lupinix@mailbox.org> - 2.5.20160926130800-1
- initial package
