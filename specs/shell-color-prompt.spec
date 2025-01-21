Name:           shell-color-prompt
Version:        0.5
Release:        3%{?dist}
Summary:        Color prompt for bash shell

License:        GPL-2.0-or-later
URL:            https://src.fedoraproject.org/rpms/shell-color-prompt
Source0:        bash-color-prompt.sh
Source1:        README.md
Source2:        COPYING
BuildArch:      noarch

%description
Default colored bash prompt.

%package -n bash-color-prompt
Summary:        Color prompt for bash shell

%description -n bash-color-prompt
Default colored bash prompt.


%prep
%setup -c -T
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} .


%build
%{nil}

%install
%global profiledir %{_sysconfdir}/profile.d

install -m 644 -D -t %{buildroot}%{profiledir} bash-color-prompt.sh


%files -n bash-color-prompt
%license COPYING
%doc README.md
%{profiledir}/bash-color-prompt.sh


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Jens Petersen <petersen@redhat.com> - 0.5-1
- require interactive bash session
- new PROMPT_HIGHLIGHT is appended to PROMPT_COLOR and PROMPT_DIR_COLOR
- try to use local variables
- new functions: prompt_setup_color_ps1(), prompt_color(),
  prompt_default_highlight(), prompt_default_color(), prompt_dir_color(),
  prompt_default_format(), prompt_os_color(), prompt_container(),
  prompt_no_color(), prompt_highlight(), prompt_no_highlight(),
  prompt_plain(), prompt_traditional_format(), prompt_reset_traditional_ps1()
- prompt_os_color() replaces prompt_default_os()
- prepend hexagon if $container defined
- for Gnome default PROMPT_HIGHLIGHT=1 for bold prompt (#2293059)

* Fri Jun  7 2024 Jens Petersen <petersen@redhat.com> - 0.4.2-1
- test for BASH_VERSION to avoid running for other shells
  (#2279643, Nathan Grennan)
- fix condition regression introduced with 0.4.1 linux console change
- rename prompt_color_force variable to bash_prompt_color_force

* Thu Jan 25 2024 Jens Petersen <petersen@redhat.com> - 0.4.1-1
- also enable for Linux console (TERM=linux)

* Mon Nov 13 2023 Jens Petersen <petersen@redhat.com> - 0.4-1
- define PROMPT_COLOR
- add PROMPT_USERHOST default variable
- add colorpre and colorsuf variables
- drop PROMPT_ERROR
- drop built-in container support for now
- reset color after $ prompt
- only define default functions if setting PS1

* Mon Nov 13 2023 Jens Petersen <petersen@redhat.com> - 0.3-1
- add PROMPT_SEPARATOR and PROMPT_DIRECTORY default variables (#2239152)
- add optional PROMPT_START and PROMPT_END (replaces PROMPT_BRACKETS)
- add prompt_default(), prompt_traditional(), and prompt_default_os()
- expand README.md

* Sat Nov 11 2023 Jens Petersen <petersen@redhat.com> - 0.2.1-1
- add a container ⬢ symbol prefix

* Fri Nov 10 2023 Jens Petersen <petersen@redhat.com> - 0.2-1
- add PROMPT_DIR_COLOR to change the dir color (Thomas Steenholdt, #2239152)
- also check for bash default prompt for login shell (Sam Morris, #2248853)
- add PROMPT_BRACKETS to surround the prompt with traditional brackets
  (based on feedback from Thomas Steenholdt, #2239152)

* Thu Nov  9 2023 Jens Petersen <petersen@redhat.com> - 0.1.1-1
- only show error code if PROMPT_ERROR set

* Tue Aug 15 2023 Jens Petersen <petersen@redhat.com> - 0.1-6
- rename source package to shell-color-prompt

* Tue Jun 27 2023 Jens Petersen <petersen@redhat.com> - 0.1-5
- the colon separator is now uncolored

* Tue Jun 27 2023 Jens Petersen <petersen@redhat.com> - 0.1-4
- revert default to normal green (not bright/bold)
- set prompt_color_force to override interactive terminal checks
- drop bold from red error code

* Tue Jun 27 2023 Jens Petersen <petersen@redhat.com> - 0.1-3
- quote TERM expansion in conditional

* Tue Jun 27 2023 Jens Petersen <petersen@redhat.com> - 0.1-2
- change default to dim reverse video

* Mon Jun 26 2023 Jens Petersen <petersen@redhat.com>
- initial poc with bold green default
