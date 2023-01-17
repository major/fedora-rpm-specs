# This specfile is licensed under:
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: Fedora Project Authors
# SPDX-FileCopyrightText: 2022 Maxwell G <gotmax@e.email>
# See %%{name}.spec.license for the full license text.

%bcond_without tests

Name:           yt-dlp
Version:        2023.01.06
Release:        1%{?dist}
Summary:        A command-line program to download videos from online video platforms

License:        Unlicense
URL:            https://github.com/%{name}/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# License of the specfile
Source:         yt-dlp.spec.license

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# Needed for %%check
BuildRequires:  %{py3_dist pytest}
%endif

# Needed for docs
BuildRequires:  pandoc
BuildRequires:  make

%if 0%{?fedora} >= 36
# ffmpeg-free is now available in Fedora.
Recommends:     /usr/bin/ffmpeg /usr/bin/ffprobe
%endif

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
%autosetup

find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +

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
* Tue Jan 10 2023 Maxwell G <gotmax@e.email> - 2023.01.06-1
- Update to 2023.01.06. Fixes rhbz#2157879.

* Mon Nov 14 2022 Maxwell G <gotmax@e.email> - 2022.11.11-1
- Update to 2022.11.11. Fixes rhbz#2142417.

* Sat Oct 08 2022 Maxwell G <gotmax@e.email> - 2022.10.04-1
- Update to 2022.10.04. Fixes rhbz#2132726.

* Fri Sep 02 2022 Maxwell G <gotmax@e.email> - 2022.09.01-1
- Update to 2022.09.01. Fixes rhbz#2123442.

* Fri Aug 19 2022 Maxwell G <gotmax@e.email> - 2022.08.19-1
- Update to 2022.08.19. Fixes rhbz#2118224.

* Tue Aug 09 2022 Maxwell G <gotmax@e.email> - 2022.08.08-1
- Update to 2022.08.08.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.06.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Maxwell G <gotmax@e.email> - 2022.06.29-2
- Fix shell completions subpackages

* Mon Jul 04 2022 Maxwell G <gotmax@e.email> - 2022.06.29-1
- Update to 2022.06.29. Fixes rhbz#2102238.

* Thu Jun 23 2022 Maxwell G <gotmax@e.email> - 2022.06.22.1-1
- Update to 2022.06.22.1. Fixes rhbz#2100019.

* Fri Jun 17 2022 Maxwell G <gotmax@e.email> - 2022.05.18-3
- Fix gating configuration

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 2022.05.18-2
- Rebuilt for Python 3.11

* Tue May 24 2022 Maxwell G <gotmax@e.email> - 2022.05.18-1
- Update to 2022.05.18. Fixes rhbz#2088564.

* Fri Apr 08 2022 Maxwell G <gotmax@e.email> - 2022.04.08-1
- Update to 2022.04.08. Fixes rhbz#2073359.

* Sat Mar 12 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2022.03.08.1-2
- build: Make ffmpeg and ffprobe conditional deps for >= f36 only

* Thu Mar 10 2022 Maxwell G <gotmax@e.email> - 2022.03.08.1-1
- Update to 2022.03.08.1. Fixes rhbz#2061973.

* Mon Mar 07 2022 Maxwell G <gotmax@e.email> - 2022.02.04-2
- Add weak dependency on ffmpeg and ffprobe.
- Make shell-completion subpackages optional again.

* Fri Feb 04 2022 Maxwell G <gotmax@e.email> - 2022.2.4-1
- Update to 2022.2.4. Fixes rhbz#2050497.

* Mon Jan 24 2022 Maxwell G <gotmax@e.email> - 2022.01.21-1
- Update to 2022.01.21.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.12.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Maxwell G <gotmax@e.email> - 2021.12.27-1
- Update to 2021.12.27.

* Sun Dec 26 2021 Maxwell G <gotmax@e.email> - 2021.12.25-1
- Update to 2021.12.25.

* Wed Dec 01 2021 Maxwell G <gotmax@e.email> - 2021.12.01-1
- Update to 2021.12.01.

* Tue Nov 9 2021 Maxwell G <gotmax@e.email> - 2021.11.10.1-1
- Update to 2021.11.10.1.

* Tue Nov 9 2021 Maxwell G <gotmax@e.email> - 2021.10.22-2
- Skip installing unnecessary tox dependencies
- Fix shell-completion subpackages
- Only package README.md; don't generate extra README.txt

* Sat Oct 23 2021 Maxwell G <gotmax@e.email> - 2021.10.22-1
- Update to 2021.10.22

* Sun Oct 10 2021 Maxwell G <gotmax@e.email> - 2021.10.10-1
- Mark LICENSE with %%license instead of %%doc
- Update to 2021.10.10
- Fix non-executable-script rpmlint error
- Use `python3dist(NAME)` for dependencies
- Fix rpm-buildroot-usage rpmlint error

* Sat Oct 9 2021 Maxwell G <gotmax@e.email> - 2021.10.09-1
- Initial package
