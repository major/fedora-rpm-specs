# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Fedora Project Authors
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# License text: https://spdx.org/licenses/MIT.html

%bcond tests 1
# Whether yt-dlp-ejs support is available.
# We cannot build yt-dlp-ejs for Fedora 43 because the packaged esbuild version is too old.
%bcond ejs %[ 0%{?fedora} >= 44 ]

# Remove -s from shebang so users can install extra deps or plugins using pip.
%undefine _py3_shebang_s


Name:           yt-dlp
Version:        2026.08.19
Release:        %autorelease
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/yt-dlp/yt-dlp
Source0:        %{url}/archive/%{version}/yt-dlp-%{version}.tar.gz
Source1:        yt-dlp.conf

# https://github.com/yt-dlp/yt-dlp/pull/17491
# Relax handshake error regexp
Patch:          17491.patch

# Needed for compatibility with Fedora <= 44
Patch:          0002-Restore-compatibility-with-pytest-9.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  tomcli

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
%autosetup -p1

# Filter out ejs if the bcond is disabled
%if %{without ejs}
tomcli set pyproject.toml arrays delitem \
    project.optional-dependencies.default 'yt-dlp-ejs.*'
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

# This is only relevant when ejs support is available.
%if %{with ejs}
install -Dpm 644 %{S:1} %{buildroot}%{_sysconfdir}/yt-dlp.conf
%endif


%check
%if %{with tests}
%pytest -k "not download and not test_verify_cert[Websockets]"
%endif


%files -f %{pyproject_files}
%doc README.md
%if %{with ejs}
%config(noreplace) %{_sysconfdir}/yt-dlp.conf
%endif
%license LICENSE
%{_bindir}/yt-dlp
%{_mandir}/man1/yt-dlp.1*
%{bash_completions_dir}/yt-dlp
%{fish_completions_dir}/yt-dlp.fish
%{zsh_completions_dir}/_yt-dlp


%pyproject_extras_subpkg -n yt-dlp default secretstorage


%changelog
%autochangelog
