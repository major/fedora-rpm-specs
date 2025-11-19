# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Fedora Project Authors
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# License text: https://spdx.org/licenses/MIT.html

%bcond_without tests

Name:           yt-dlp
Version:        2025.10.22
Release:        %autorelease
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/yt-dlp/yt-dlp
Source:         %{url}/archive/%{version}/yt-dlp-%{version}.tar.gz

# https://github.com/yt-dlp/yt-dlp/commit/6f9e6537434562d513d0c9b68ced8a61ade94a64
# [rh:websockets] Upgrade websockets to 13.0 (#10815)
# Revert this patch for compatibility with older Fedora versions
# This patch is applied conditionally to Fedora <= 41
Patch1000:      0001-Revert-rh-websockets-Upgrade-websockets-to-13.0-1081.patch
# https://github.com/yt-dlp/yt-dlp/commit/c2ff2dbaec7929015373fe002e9bd4849931a4ce
# [rh:requests] Work around partial read dropping data (#13599)
# Revert this patch for compatibility with older Fedora versions
# This patch is applied conditionally to Fedora <= 41
Patch1001:      0001-Revert-rh-requests-Work-around-partial-read-dropping.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# Needed for %%check
BuildRequires:  %{py3_dist pytest}
%endif

# Needed for docs
BuildRequires:  pandoc
BuildRequires:  make

Requires:       yt-dlp+default = %{?epoch:%{epoch}:}%{version}-%{release}

# ffmpeg-free is now available in Fedora.
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe

Suggests:       python3dist(keyring)

# START: Remove in Fedora 46
Provides:       yt-dlp-bash-completion = %{version}-%{release}
Obsoletes:      yt-dlp-bash-completion < 2025.09.26-2

Provides:       yt-dlp-fish-completion = %{version}-%{release}
Obsoletes:      yt-dlp-fish-completion < 2025.09.26-2

Provides:       yt-dlp-zsh-completion = %{version}-%{release}
Obsoletes:      yt-dlp-zsh-completion < 2025.09.26-2
# END: Remove in Fedora 46

%description
yt-dlp is a command-line program to download videos from many different online
video platforms, such as youtube.com. The project is a fork of youtube-dl with
additional features and fixes.


%prep
%autosetup -N
%autopatch -M 999 -p1
%if %{defined fedora} && 0%{?fedora} <= 41
# Revert patch for compatibility with older websockets
%autopatch -m 1000 -p1
%endif

# Remove unnecessary shebangs
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +


%generate_buildrequires
%pyproject_buildrequires -x default,secretstorage


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
%pytest -k "not download and not test_verify_cert[Websockets]"
%endif


%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/yt-dlp
%{_mandir}/man1/yt-dlp.1*
%{bash_completions_dir}/yt-dlp
%{fish_completions_dir}/yt-dlp.fish
%{zsh_completions_dir}/_yt-dlp


%pyproject_extras_subpkg -n yt-dlp default secretstorage


%changelog
%autochangelog
