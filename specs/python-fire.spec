Name:           python-fire
Version:        0.7.1
Release:        %autorelease
Summary:        A library for automatically generating command line interfaces

License:        Apache-2.0
URL:            https://github.com/google/python-fire
Source:         %{pypi_source fire}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(levenshtein)

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
Python Fire is a library for automatically generating command
line interfaces (CLIs) from absolutely any Python object.

* Python Fire is a simple way to create a CLI in Python.
* Python Fire is a helpful tool for developing and
  debugging Python code.
* Python Fire helps with exploring existing code or turning
  other people's code into a CLI.
* Python Fire makes transitioning between Bash and Python
  easier.
* Python Fire makes using a Python REPL easier by setting up
  the REPL with the modules and variables you'll need already
  imported and created.
}

%description %_description

%package -n     python3-fire
Summary:        %{summary}

%description -n python3-fire %_description

%prep
%autosetup -p1 -n fire-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l fire

%check
%pyproject_check_import

%files -n python3-fire -f %{pyproject_files}

%changelog
%autochangelog
