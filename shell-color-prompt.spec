Name:           shell-color-prompt
Version:        0.4
Release:        1%{?dist}
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
