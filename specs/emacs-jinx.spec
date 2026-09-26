%global elpa_name jinx
%global emacs_version_with_archsitelispdir 1:30.2-9

Name:           emacs-%{elpa_name}
Version:        2.10
Release:        %{autorelease}
Summary:        Fast just-in-time spell-checker for Emacs
License:        GPL-3.0-or-later
URL:            https://github.com/minad/%{elpa_name}
Source:         https://elpa.gnu.org/packages/%{elpa_name}-%{version}.tar.lz

BuildRequires:  /usr/bin/pkg-config
BuildRequires:  emacs-devel
BuildRequires:  emacs-nw >= %{emacs_version_with_archsitelispdir}
BuildRequires:  enchant2-devel
BuildRequires:  gcc
BuildRequires:  lzip

Requires:       emacs(bin) >= %{emacs_version_with_archsitelispdir}
Requires:       emacs(bin)%{?_emacs_version: >= 1:%{_emacs_version}}

%description
Jinx is a fast just-in-time spell-checker for Emacs. Jinx highlights
misspelled words in the text of the visible portion of the buffer. For
efficiency, Jinx highlights misspellings lazily, recognizes window
boundaries and text folding, if any.


%prep
%autosetup -n %{elpa_name}-%{version}


%build
%{__cc} \
 $(emacs --batch --load=%{elpa_name}.el \
         --eval '(dolist (arg jinx--compile-flags) (princ (concat arg " ")))') \
 %{build_cflags} \
 $(pkg-config --cflags --libs enchant-2) \
 -o %{elpa_name}-mod.so %{elpa_name}-mod.c


%install
install -d %{buildroot}%{_emacs_archsitelispdir}/
install -m 0755 %{elpa_name}-mod.so %{buildroot}%{_emacs_archsitelispdir}/

rm emacs-module.h \
   %{elpa_name}-mod.c \
   %{elpa_name}-mod.so

emacs --batch \
      --eval '(let ((package-user-dir "%{buildroot}%{_emacs_sitelispdir}/elpa"))
                (package-install-file (or (pop argv) default-directory)))'


%files
%{_emacs_archsitelispdir}/%{elpa_name}-mod.so
%dir %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}
%doc %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/NEWS.org
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/README-elpa
%doc %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/README.org
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/dir
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}-autoloads.el
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}-pkg.el
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}.el
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}.elc
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}.info
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/news


%changelog
%{autochangelog}
