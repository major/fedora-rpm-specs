#%%global gittag 1.7.0
%global commit ffc806dc71288c615c6bcd8bd267f75f56daa8b1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20230223

# Disable debuginfo generation, no executable or library is built
%global debug_package %{nil}

Name:           celestia-data
%if "%{?gittag}"
Version:        1.7.0
%else
Version:        1.7.0~%{date}%{shortcommit}
%endif
Release:        %autorelease
Summary:        Data, models and textures for Celestia
# An accurate description of content licensing is available in the README file
License:        GPL-2.0-or-later AND CC-BY-SA-4.0 AND JPL-image
URL:            https://celestia.space/
%if "%{?gittag}"
Source0:        https://github.com/CelestiaProject/CelestiaContent/archive/%{gittag}/CelestiaContent-%{version}.tar.gz
%else
Source0:        https://github.com/CelestiaProject/CelestiaContent/archive/%{commit}/CelestiaContent-%{commit}.tar.gz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  gettext-devel

Requires:       celestia > 1.6.2


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
