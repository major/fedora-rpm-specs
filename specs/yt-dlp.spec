# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Fedora Project Authors
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# See yt-dlp.spec.license for the full license text.

%bcond_without tests

Name:           yt-dlp
Version:        2025.06.09
Release:        %autorelease
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/yt-dlp/yt-dlp
Source:         %{url}/archive/%{version}/yt-dlp-%{version}.tar.gz
# License of the specfile
Source:         yt-dlp.spec.license

# [test] `traversal`: Fix morsel tests for Python 3.14 (#13471)
# https://github.com/yt-dlp/yt-dlp/pull/13471
#
# https://github.com/yt-dlp/yt-dlp/issues/13452
# test_traversal_morsel fails on Python 3.14
#
# https://bugzilla.redhat.com/2345522
Patch:          0001-test-traversal-Fix-morsel-tests-for-Python-3.14-1347.patch

# https://github.com/yt-dlp/yt-dlp/commit/6f9e6537434562d513d0c9b68ced8a61ade94a64
# [rh:websockets] Upgrade websockets to 13.0 (#10815)
# Revert this patch for compatibility with older Fedora versions
# This patch is applied conditionally to Fedora <= 41
Patch1000:      0001-Revert-rh-websockets-Upgrade-websockets-to-13.0-1081.patch

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

%global _description %{expand:
yt-dlp is a command-line program to download videos from many different online
video platforms, such as youtube.com. The project is a fork of youtube-dl with
additional features and fixes.}

%description %{_description}

%package bash-completion
Summary:        Bash completion for yt-dlp
Requires:       yt-dlp = %{version}-%{release}
Requires:       bash-completion
Supplements:    (yt-dlp and bash-completion)

%description bash-completion
Bash command line completion support for yt-dlp.

%package zsh-completion
Summary:        Zsh completion for yt-dlp
Requires:       yt-dlp = %{version}-%{release}
Requires:       zsh
Supplements:    (yt-dlp and zsh)

%description zsh-completion
Zsh command line completion support for yt-dlp.

%package fish-completion
Summary:        Fish completion for yt-dlp
Requires:       yt-dlp = %{version}-%{release}
Requires:       fish
Supplements:    (yt-dlp and fish)

%description fish-completion
Fish command line completion support for yt-dlp.

%prep
%autosetup -N
%autopatch -M 999 -p1
%if %{defined fedora} && 0%{?fedora} <= 41
# Revert patch for compatibility with older websockets
%autopatch 1000 -p1
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
%{_bindir}/yt-dlp
%{_mandir}/man1/yt-dlp.1*
%doc README.md
%license LICENSE

%files bash-completion
%{bash_completions_dir}/yt-dlp

%files zsh-completion
%{zsh_completions_dir}/_yt-dlp

%files fish-completion
%{fish_completions_dir}/yt-dlp.fish

%pyproject_extras_subpkg -n yt-dlp default secretstorage

%changelog
%autochangelog
