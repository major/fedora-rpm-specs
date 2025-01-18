Name:		editorconfig-emacs
Version:	0.10.1
Release:	3%{?dist}
Summary:	EditorConfig plugin for emacs
License:	GPL-3.0-or-later
URL:		https://github.com/editorconfig/%{name}
Source0:	https://github.com/editorconfig/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	editorconfig-init.el
BuildRequires:	emacs
BuildRequires:	texinfo
BuildArch:	noarch
Requires:	emacs(bin) >= %{_emacs_version}

%description
This is the EditorConfig plugin for emacs.  With this plugin
installed, emacs will automatically respect coding style settings
found in an .editorconfig file.

%prep
%autosetup

%build

# The tarball includes an Eask file, but eask is not packaged for
# Fedora (and is unlikely to be, since it depends on multiple NPM
# modules).  Use a direct %{_emacs_bytecompile} instead.
#
%{_emacs_bytecompile} *.el

# Build info page
#
make doc/editorconfig.info

%install
%{__mkdir_p} %{buildroot}%{_emacs_sitelispdir}
%{__install} -p -m 644 *.el *.elc %{buildroot}%{_emacs_sitelispdir}/
%{__mkdir_p} %{buildroot}%{_emacs_sitestartdir}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/
%{__mkdir_p} %{buildroot}%{_infodir}
%{__install} -p -m 644 doc/editorconfig.info %{buildroot}%{_infodir}/

%files
%doc CONTRIBUTORS CHANGELOG.md README.md
%license LICENSE
%{_emacs_sitelispdir}/editorconfig*.el
%{_emacs_sitelispdir}/editorconfig*.elc
%{_emacs_sitestartdir}/editorconfig-init.el
%{_infodir}/editorconfig*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 12 2024 Michael Brown <mbrown@fensystems.co.uk> - 0.10.1-1
- Initial package
