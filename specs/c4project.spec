%global commit 386e367dfa5369289f706d70c6790fefc099dd27
%global snapdate 20250124

Name:           c4project
Summary:        Useful CMake scripts
# This project has never been assigned a version. The author really intends it
# for use as a git submodule rather than for system-wide installation.
Version:        0^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease

URL:            https://github.com/biojppm/cmake
# The entire source is MIT, except Toolchain-PS4.cmake and
# Toolchain-XBoxOne.cmake, which are Apache-2.0.
License:        MIT AND Apache-2.0
Source:         %{url}/archive/%{commit}/cmake-%{commit}.tar.gz

BuildArch:      noarch

Requires:       cmake-filesystem
Requires:       git-core

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%prep
%autosetup -n cmake-%{commit}

# For now, we elect not to install the “bm-xp” browser-based benchmark explorer
# tool. It would be inconvenient to package this in a way that was useful in
# practice, and it’s not required by any of the CMake macros that are the real
# point of packaging this.
rm -rvf 'bm-xp'


%build
# Nothing to do


%install
install -d '%{buildroot}%{_datadir}/cmake/c4project'
# We install a copy of the repository, but we don’t want to include dotfiles or
# duplicate the README and LICENSE files.
find . -mindepth 1 -maxdepth 1 ! -name '.*' \( -type d -o \
    -type f ! -name 'README.md' ! -name 'LICENSE.txt' \) \
    -execdir cp -vrp '{}' '%{buildroot}%{_datadir}/cmake/c4project' ';'


%check
# No upstream tests


%files
%license LICENSE.txt
%doc README.md

%{_datadir}/cmake/c4project


%changelog
%autochangelog
