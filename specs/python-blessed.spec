%global pypi_name blessed
%global summary A thin, practical wrapper around terminal capabilities in Python
%global _description \
Blessed is a thin, practical wrapper around terminal styling, screen \
positioning, and keyboard input. \
\
It provides: \
- Styles, color, and maybe a little positioning without necessarily clearing \
  the whole screen first. \
- Works great with standard Python string formatting. \
- Provides up-to-the-moment terminal height and width, so you can respond \
  to terminal size changes. \
- Avoids making a mess if the output gets piped to a non-terminal: outputs \
  to any file-like object such as StringIO, files, or pipes. \
- Uses the terminfo(5) database so it works with any terminal type and \
  supports any terminal capability: No more C-like calls to tigetstr and \
  tparm. \
- Keeps a minimum of internal state, so you can feel free to mix and match \
  with calls to curses or whatever other terminal libraries you like. \
- Provides plenty of context managers to safely express terminal modes, \
  automatically restoring the terminal to a safe state on exit. \
- Act intelligently when somebody redirects your output to a file, omitting \
  all of the terminal sequences such as styling, colors, or positioning. \
- Dead-simple keyboard handling: safely decoding unicode input in your \
  system’s preferred locale and supports application/arrow keys. \
- Allows the printable length of strings containing sequences to be \
  determined.

Name:       python-%{pypi_name}
Version:    1.38.0
Release:    %autorelease
Summary:    %{summary}

License:    MIT
URL:        https://github.com/jquast/blessed
Source0:    %{pypi_source}
BuildArch:  noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description %{_description}



%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

mkdir -p %{buildroot}%{_docdir}/%{name}/
(cd docs && find -name "*.rst" -exec cp --parents {} %{buildroot}%{_docdir}/%{name}/ \;)

%check
PYTHONIOENCODING=UTF8 TERM=xterm-256color %pytest --verbose --verbose --exitfirst -c /dev/null


%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc %{_docdir}/%{name}

%changelog
%autochangelog
