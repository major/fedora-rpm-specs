%global elpa_name rpm-spec-mode

Name:           emacs-%{elpa_name}
Version:        0.16.0.20260616.59
Release:        %autorelease
Summary:        Major GNU Emacs mode for editing RPM spec files
License:        GPL-2.0-or-later
URL:            https://github.com/Thaodan/%{elpa_name}
VCS:            git:%{url}.git
Source0:        https://elpa.nongnu.org/nongnu-devel/rpm-spec-mode-0.16.0.20260616.59.tar.lz

BuildArch:      noarch
BuildRequires:  emacs-nw
BuildRequires:  lzip
Requires:       emacs(bin) >= %{?_emacs_version}%{!?_emacs_version:0}

%description
Major GNU Emacs mode for editing RPM spec files.


%prep
%autosetup -n %{elpa_name}-%{version}


%install
emacs --batch \
      --eval '(let ((package-user-dir "%{buildroot}%{_emacs_sitelispdir}/elpa"))
                (package-install-file (or (pop argv) default-directory)))'


%files
%dir %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}
%doc %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/ChangeLog
%doc %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/README.org
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/README-elpa
%license %{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/LICENSE
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}-pkg.el
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}-autoloads.el
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}.elc
%{_emacs_sitelispdir}/elpa/%{elpa_name}-%{version}/%{elpa_name}.el


%changelog
%autochangelog
