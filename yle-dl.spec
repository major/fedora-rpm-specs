Name:           yle-dl
Version:        20221231
Release:        %autorelease
Summary:        Download videos from Yle servers

License:        GPL-3.0-or-later
URL:            https://aajanki.github.io/yle-dl/index-en.html
Source:         https://github.com/aajanki/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       /usr/bin/ffmpeg
# According to README, needed "optionally for few rare streams".
Recommends:     wget

%description
Command-line program for downloading media files from the video streaming
services of the Finnish national broadcasting company Yle: Yle Areena,
Elävä arkisto, and Yle news. The videos are saved in Matroska (.mkv) or MP4
format.

%prep
%autosetup -p1 -n %{name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


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
