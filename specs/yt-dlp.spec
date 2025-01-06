# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Fedora Project Authors
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# See %%{name}.spec.license for the full license text.

%bcond_without tests

Name:           yt-dlp
Version:        2024.12.23
Release:        %autorelease
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/%{name}/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# License of the specfile
Source:         yt-dlp.spec.license

# https://github.com/yt-dlp/yt-dlp/commit/6f9e6537434562d513d0c9b68ced8a61ade94a64
# [rh:websockets] Upgrade websockets to 13.0 (#10815)
# Revert this patch for compatibility with older Fedora versions
Patch1000:      websockets-13.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Needed for %%prep
BuildRequires:  tomcli

%if %{with tests}
# Needed for %%check
BuildRequires:  %{py3_dist pytest}
%endif

# Needed for docs
BuildRequires:  pandoc
BuildRequires:  make

# ffmpeg-free is now available in Fedora.
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe

Suggests:       python3dist(keyring)

%global _description %{expand:
yt-dlp is a command-line program to download videos from many different online
video platforms, such as youtube.com. The project is a fork of youtube-dl with
additional features and fixes.}

%description %{_description}

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       fish
Supplements:    (%{name} and fish)

%description fish-completion
Fish command line completion support for %{name}.

%prep
%autosetup -N
%if %{defined fedora} && 0%{?fedora} <= 41
# Revert patch for compatibility with older websockets
%patch -P1000 -p1 -R
%endif

# Remove unnecessary shebangs
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
# Relax version constraints
tomcli-set pyproject.toml lists replace project.dependencies \
    '(requests|urllib3|websockets)>=.*' '\1'

%generate_buildrequires
%pyproject_buildrequires -r

%build
# Docs and shell completions
make yt-dlp.1 completion-bash completion-zsh completion-fish

# Docs and shell completions are also included in the wheel.
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files yt_dlp

%check
%if %{with tests}
# See https://github.com/yt-dlp/yt-dlp/blob/master/devscripts/run_tests.sh
%pytest -k "not download"
%endif

%files -f %{pyproject_files}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%doc README.md
%license LICENSE

%files bash-completion
%{bash_completions_dir}/%{name}

%files zsh-completion
%{zsh_completions_dir}/_%{name}

%files fish-completion
%{fish_completions_dir}/%{name}.fish

%changelog
%autochangelog
