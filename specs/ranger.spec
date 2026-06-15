Name:           ranger
Version:        1.9.4
Release:        %autorelease
Summary:        A vim-like file manager
License:        GPL-3.0-only
URL:            https://ranger.fm/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel


%description
Ranger is a free console file manager that gives you greater flexibility and a
good overview of your files without having to leave your *nix console. It
visualizes the directory tree in two dimensions: the directory hierarchy on
one, lists of files on the other, with a preview to the right so you know where
you'll be going.


%prep
%autosetup
# Fix shebang in the main executable script
%{__python3} /usr/lib/rpm/redhat/pathfix.py -pn -i %{__python3} %{name}.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l '*'
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_pkgdocdir} _doc
find _doc -type f -exec chmod -R -x '{}' \;

# Remove shebang from the python module to satisfy rpmlint
sed -i -e '1{\@^#!@d}' %{buildroot}%{python3_sitelib}/%{name}/ext/rifle.py


%check
%pyproject_check_import


%files -f %{pyproject_files}
%doc _doc/*
%{_bindir}/ranger
%{_bindir}/rifle
%{_datadir}/applications/ranger.desktop
%{_mandir}/man1/ranger.1*
%{_mandir}/man1/rifle.1*


%changelog
%autochangelog
