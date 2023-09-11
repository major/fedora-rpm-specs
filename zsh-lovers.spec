Name:           zsh-lovers
Version:        0.10.0
Release:        %autorelease
Summary:        A collection of tips, tricks and examples for the Z shell
License:        GPLv2
URL:            https://grml.org/zsh/#zshlovers
Source0:        https://deb.grml.org/pool/main/z/zsh-lovers/zsh-lovers_%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  asciidoc

%description
zsh-lovers is a small project which tries to collect tips, tricks and examples
for the Z shell. 

This package only ships a manpage of the collection.

%prep
%autosetup

%build
a2x -vv -L -f manpage zsh-lovers.1.txt

%install
install -pDm644 zsh-lovers.1 %{buildroot}%{_mandir}/man1/zsh-lovers.1

%files
%doc README.md
%license COPYING
%{_mandir}/man1/zsh-lovers.1*

%changelog
%autochangelog
