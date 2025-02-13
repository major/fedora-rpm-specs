%global sum A scientific image viewer and toolkit
%global _description %{expand:
Ginga is a toolkit designed for building viewers for scientific image data in 
Python, visualizing 2D pixel data in numpy arrays. It can view astronomical 
data such as contained in files based on the FITS (Flexible Image Transport
System) file format. It is written and is maintained by software engineers at 
the Subaru Telescope, National Astronomical Observatory of Japan.             
                                                                              
The Ginga toolkit centers around an image display class which supports zooming
and panning, color and intensity mapping, a choice of several automatic cut  
levels algorithms and canvases for plotting scalable geometric forms. In 
addition to this widget, a general purpose “reference” FITS viewer is 
provided, based on a plugin framework. A fairly complete set of standard 
plugins are provided for features that we expect from a modern FITS viewer:
panning and zooming windows, star catalog access, cuts, star pick/fwhm,
thumbnails, etc.}

Name:           ginga
Version:        5.2.0
Release:        %autorelease
Summary:        %{sum}
# License breakdown
#
# In general (if not listed below): BSD
#
# Apache 2.0
#   ginga/util/heaptimer.py
# 
License:        BSD-3-Clause AND Apache-2.0
URL:            https://ejeschke.github.io/ginga/
Source0:        %{pypi_source}

# General build reqs
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
Requires:       python3-%{name} = %{version}-%{release}

BuildArch:      noarch

%description %_description

%package -n python3-%{name}
Summary:        %{sum}
Requires:       google-roboto-fonts
Requires:       google-roboto-condensed-fonts

%description -n python3-%{name} %_description 

%package -n python3-%{name}-examples
Summary:        Examples for %{name}
Requires:       python3-%{name} = %{version}-%{release}

%description -n python3-%{name}-examples
Examples for %{name}

%pyproject_extras_subpkg -n python3-ginga recommended
%pyproject_extras_subpkg -n python3-ginga qt5

%prep
%autosetup
sed -i -e s/opencv-python-headless/opencv/ -e s/python-magic.*/file-magic/ setup.cfg

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
%autochangelog
