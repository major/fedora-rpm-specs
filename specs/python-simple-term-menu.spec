Name:           python-simple-term-menu
Version:        1.6.6
Release:        %autorelease
Summary:        A Python package which creates simple interactive menus on the command line

License:        MIT
URL:            https://github.com/IngoMeyer441/simple-term-menu
Source:         %{pypi_source simple_term_menu}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
simple-term-menu creates simple menus for interactive command line programs. It
can be used to offer a choice of different options to the user. Menu entries
can be selected with the arrow, j/k, or emacs (C-n/C-p) keys. The module uses
the terminfo database to detect terminal features automatically and disables
styles that are not available. Currently, Linux and macOS are supported.}

%description %_description

%package -n     python3-simple-term-menu
Summary:        %{summary}

%description -n python3-simple-term-menu %_description


%prep
%autosetup -p1 -n simple_term_menu-%{version}

# Remove unnecessary shebang
sed -i '1{/^#!/d}' simple_term_menu.py
chmod 644 simple_term_menu.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l simple_term_menu


%check
%pyproject_check_import


%files -n python3-simple-term-menu -f %{pyproject_files}
%doc README.md
%{_bindir}/simple-term-menu


%changelog
%autochangelog
