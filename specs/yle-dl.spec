Name:           yle-dl
Version:        20250126
Release:        %autorelease
Summary:        Download videos from Yle servers

License:        GPL-3.0-or-later
URL:            https://aajanki.github.io/yle-dl/index-en.html
Source:         https://github.com/aajanki/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
# Depends on archful python3-xattr which excludes i686
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  /usr/bin/ffmpeg
Requires:       /usr/bin/ffmpeg
Recommends:     yle-dl+extra
# According to README, "required for podcasts".
Recommends:     wget

%description
Command-line program for downloading media files from the video streaming
services of the Finnish national broadcasting company Yle: Yle Areena,
Elävä arkisto, and Yle news. The videos are saved in Matroska (.mkv) or MP4
format.


# Enables storing video metadata as extended file attributes
# and automatically detecting filesystems that require restricted character sets.
%pyproject_extras_subpkg -n yle-dl extra


%prep
%autosetup -p1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x extra -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files yledl


%check
%pytest --ignore=tests/integration


%files -f %{pyproject_files}
%doc README.*
%license COPYING
%{_bindir}/yle-dl


%changelog
%autochangelog
