#%%global gittag 1.7.0
%global commit db53ae319ffc06d2d6fe92d2b65d210fdae7bd67
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20231125

# Disable debuginfo generation, no executable or library is built
%global debug_package %{nil}

Name:           celestia-data
%if "%{?gittag}"
Version:        1.7.0
%else
# This is a really dirty hack to overcome a wrong update path due to git commit hash
# previously applied without '.git'.
# I don't want to bump Epoch, so I'm going to add a leading '3' before %%{date}
# until version 1.7.0 is finally released.
Version:        1.7.0~3%{date}.git%{shortcommit}
%endif
Release:        %autorelease
Summary:        Data, models and textures for Celestia
# An accurate description of content licensing is available in the README file
License:        GPL-2.0-or-later AND CC-BY-SA-4.0 AND JPL-image
URL:            https://celestiaproject.space/
%if "%{?gittag}"
Source0:        https://github.com/CelestiaProject/CelestiaContent/archive/%{gittag}/CelestiaContent-%{version}.tar.gz
%else
Source0:        https://github.com/CelestiaProject/CelestiaContent/archive/%{commit}/CelestiaContent-%{commit}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gettext-devel

Requires:       celestia-common > 1.6.2


%description
This package provides the required data files, spacecraft
models and planet textures for Celestia to work.


%prep
%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n CelestiaContent-%{commit} -p1
%endif


%build
%cmake
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%files -f %{name}.lang
%doc README
%license COPYING
%{_datadir}/celestia/data
%{_datadir}/celestia/extras-standard
%{_datadir}/celestia/models
%{_datadir}/celestia/textures
%{_datadir}/celestia/warp


%changelog
%autochangelog
