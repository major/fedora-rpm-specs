%global pkg agent-shell

Name:           emacs-%{pkg}
Version:        0.56.1
Release:        %autorelease
Summary:        A native Emacs buffer to interact with LLM agents powered by ACP

License:        GPL-3.0-or-later
URL:            https://github.com/xenodium/agent-shell
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        %{pkg}-init.el
# acp.el
%global acp_version 0.12.2
Source2:        https://github.com/xenodium/acp.el/archive/refs/tags/v%{acp_version}.tar.gz
# shell-maker.el
%global sm_version 0.93.1
Source3:        https://github.com/xenodium/shell-maker/archive/refs/tags/v%{sm_version}.tar.gz

BuildRequires:  emacs
Requires:       emacs-filesystem
Provides:       bundled(emacs-acp) = %{acp_version}
Provides:       bundled(emacs-shell-maker) = %{sm_version}

Requires:       emacs(bin) >= %{_emacs_version}

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n %{pkg}-%{version}
# acp.el
tar xf %{SOURCE2}
cp -p acp.el-*/LICENSE LICENSE.acp
cp -p acp.el-*/*.el .
rm -rf acp.el-*

# shell-maker.el
tar xf %{SOURCE3}
cp -p shell-maker-*/LICENSE LICENSE.shell-maker
cp -r shell-maker-*/*.el .
rm -rf shell-maker-*

%build

%install
install -dm 0755 %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 *.el -t %{buildroot}%{_emacs_sitelispdir}/%{pkg}/
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_emacs_sitestartdir}/%{pkg}-init.el

%files
%doc README.org
%license LICENSE LICENSE.acp LICENSE.shell-maker
%{_emacs_sitelispdir}/%{pkg}/
%{_emacs_sitestartdir}/*.el

%changelog
%autochangelog
