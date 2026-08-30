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

%global forgeurl https://github.com/ejeschke/ginga
Version:        7.4.0
%forgemeta

Name:           ginga
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
URL:            %{forgeurl}
Source:         %{forgesource}

# General build reqs
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  google-roboto-condensed-fonts
BuildRequires:  google-roboto-fonts
BuildRequires:  python3-pyqt6
Requires:       python3-%{name} = %{version}-%{release}

BuildArch:      noarch
Recommends:     google-roboto-condensed-fonts
Recommends:     google-roboto-fonts

%description %_description

%package -n python3-%{name}
Summary:        %{sum}
Requires:       google-roboto-condensed-fonts
Requires:       google-roboto-fonts

%description -n python3-%{name} %_description 

%package -n python3-%{name}-examples
Summary:        Examples for %{name}
Requires:       python3-%{name} = %{version}-%{release}

%description -n python3-%{name}-examples
Examples for %{name}

%pyproject_extras_subpkg -n python3-ginga recommended
%pyproject_extras_subpkg -n python3-ginga qt6

%prep
%autosetup
sed -i -e s/opencv-python-headless/opencv/ setup.cfg
# we don't have pillow-heif packaged
sed -i -e /pillow-heif/d setup.cfg

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x recommended -x qt6 -t

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_shebang_fix ginga/examples
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
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

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
export QT_API=pyqt6
%pyproject_check_import -e '*.tests*' -e 'ginga.aggw.*' -e 'ginga.gtk3w.*' -e 'ginga.gtk4w.*' -e 'ginga.tkw.*' -e 'ginga.mplw.*' -e 'ginga.opengl.*' -e 'ginga.web.*' -e 'ginga.examples.*' -e 'ginga.gw.*' -e 'ginga.rv.*' -e 'ginga.util.wcsmod.wcs_astlib' -e 'ginga.util.wcsmod.wcs_kapteyn' -e 'ginga.util.wcsmod.wcs_starlink'
%pytest

%files
%doc README.md LONG_DESC.txt doc/WhatsNew.rst
%{_bindir}/ggrc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md
# Examples are shipped as documentation in examples subpackage
%exclude %{python3_sitelib}/%{name}/examples

%files -n python3-%{name}-examples
%doc ginga/examples

%changelog
%autochangelog
