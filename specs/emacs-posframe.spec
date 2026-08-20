Name:           emacs-posframe
Version:        1.5.2
Release:        %autorelease
Summary:        Pop up a child frame at point

License:        GPL-3.0-or-later
URL:            https://github.com/tumashu/posframe
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/posframe-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  emacs-nw

Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
Posframe can pop up a frame at point.  This posframe is a child-frame
connected to its root window’s buffer.  The main advantages are:

- It is fast enough for daily usage.
- It works well with CJK languages.

%prep
%autosetup -n posframe-%{version}

%build
emacs -batch --no-init-file --no-site-file \
  --eval "(let ((backup-inhibited t)) (loaddefs-generate \".\" \"$PWD/posframe-loaddefs.el\"))"
%_emacs_bytecompile *.el

%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/posframe
install -p -m 644 *.el{,c} %{buildroot}/%{_emacs_sitelispdir}/posframe

mkdir -p %{buildroot}%{_emacs_sitestartdir}
mv %{buildroot}/%{_emacs_sitelispdir}/posframe/posframe-loaddefs.el \
   %{buildroot}%{_emacs_sitestartdir}

%files
%doc README.org snapshots
%{_emacs_sitelispdir}/posframe/
%{_emacs_sitestartdir}/posframe-loaddefs.el

%changelog
%autochangelog
