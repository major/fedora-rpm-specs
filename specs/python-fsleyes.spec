# build order for fsleyes packages:
# 1. fsleyes-widgets
# 2. fslpy
# 3. fsleyes-props
# 4. fsleyes

%global desc \
FSLeyes, the FSL image viewer

# PyPi tar does not include tests
# Upstream says the tests, since they use xvfb etc., may not always pass on all
# platforms.
%bcond_with xvfb_tests

%global forgeurl https://github.com/pauldmccarthy/fsleyes

Name:           python-fsleyes
Version:        1.15.0
Release:        %autorelease
Summary:        FSLeyes, the FSL image viewer

%global tag %{version}
%forgemeta

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%description
%{desc}

%package -n python3-fsleyes
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  /usr/bin/desktop-file-install
BuildRequires:  /usr/bin/appstream-util
Requires:       hicolor-icon-theme
# from requirements-dev.txt

%if %{with xvfb_tests}
BuildRequires:  graphviz
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-cov}
BuildRequires:  %{py3_dist wxpython}
BuildRequires:  freeglut-devel
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  python3-matplotlib-wx
%endif

Requires:       dcm2niix
Requires:       python3-matplotlib-wx

Provides:       fsleyes = %{version}-%{release}

%description -n python3-fsleyes
%{desc}

%prep
%forgesetup

# extras: not yet packaged in Fedora
sed -i -e '/"file-tree"/ d' \
    -e '/"file-tree-fsl"/ d' \
    -e '/"coverage"/ d' \
    -e '/"pytest-cov"/ d' \
    pyproject.toml

# remove unneeded shebangs
find . -name "*py" -exec sed -i '/#!\/usr\/bin\/env python/ d' '{}' \;

%generate_buildrequires
%pyproject_buildrequires -x extra -x test

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fsleyes

# install desktop file in correct location
desktop-file-install --dir=%{buildroot}%{_datadir}/applications fsleyes/assets/linux/uk.ac.ox.fmrib.FSLeyes.desktop
rm -f %{python3_sitelib}/fsleyes/assets/linux/uk.ac.ox.fmrib.FSLeyes.desktop

# install appdata file
install -p -m 0644 -D -t %{buildroot}%{_metainfodir} fsleyes/assets/linux/uk.ac.ox.fmrib.FSLeyes.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*FSLeyes*xml

rm -f %{python3_sitelib}/fsleyes/assets/linux/uk.ac.ox.fmrib.FSLeyes.appdata.xml

# install icons to the right place
pushd fsleyes/assets/icons/app_icon/fsleyes.iconset/
for size in 16 32 128 256 512
do
install -p -m 0755 -D -T "icon_${size}x${size}.png" %{buildroot}%{_datadir}/icons/hicolor/"${size}x${size}"/apps/fsleyes.png
done
# do these manually
install -p -m 0755 -D -T icon_32x32@2x.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/fsleyes.png
install -p -m 0755 -D -T icon_512x512@2x.png %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/fsleyes.png
popd
# 48x58 is in a different place than the others
install -p -m 0755 -D -t %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/ fsleyes/assets/linux/hicolor/48x48/apps/fsleyes.png


%check
export MPLBACKEND=wxagg
%if %{with xvfb_tests}
# https://github.com/pauldmccarthy/fsleyes/blob/master/.ci/test_template.sh
export FSLEYES_TEST_GL=2.1
xvfb-run -s "-screen 0 640x480x24" pytest-%{python3_version}
sleep 10
# test overlay types for GL14 as well
export FSLEYES_TEST_GL=1.4
xvfb-run -s "-screen 0 640x480x24" pytest-%{python3_version}
%endif

%files -n python3-fsleyes  -f %{pyproject_files}
%doc README.rst
%{_bindir}/fsleyes
%{_bindir}/render
%{_bindir}/fsleyes_unfiltered
%{_metainfodir}/uk.ac.ox.fmrib.FSLeyes.appdata.xml
%{_datadir}/icons/hicolor/*/apps/fsleyes.png
%{_datadir}/applications/uk.ac.ox.fmrib.FSLeyes.desktop

%changelog
%autochangelog
