Name:           python-python-multipart
Version:        0.0.21
Release:        %autorelease
Summary:        A streaming multipart parser for Python

License:        Apache-2.0
URL:            https://github.com/Kludex/python-multipart
Source:         %{pypi_source python_multipart}

BuildSystem:            pyproject
BuildOption(install):   -l python_multipart multipart

BuildArch:      noarch

# See testenv.deps from
# https://github.com/Kludex/python-multipart/blob/%%{version}/tox.ini.  Because
# of unwanted coverage dependencies and arguments, it’s not worth packaging
# from the GitHub source archive and generating test dependencies with tox;
# it’s much easier to just enumerate them manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist PyYAML}

%global common_description %{expand:
Python-Multipart is a streaming multipart parser for Python.}

%description %{common_description}


%package -n python3-python-multipart
Summary:        %{summary}

# Prior to Fedora 41, the python-multipart package provided this library,
# https://pypi.org/project/python-multipart/. In Fedora 41, the
# python-python-multipart package was introduced and python-multipart was
# repurposed for https://pypi.org/project/multipart/. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming.
#
# Prior to release 0.0.13, this package used the same import namespace (“import
# multipart”); this means there were file conflicts. This is not generally
# allowable, but there was no way to avoid it in this case. See:
#
#   Namespace conflict with multipart package
#   https://github.com/Kludex/python-multipart/issues/149
#
# Since release 0.0.13, the importable package name is python_multipart,
# resolving the file conflict. However, there is a compatibility hack that
# allows “import multipart” to keep working, giving the “real” multipart
# package if it is installed, and this package otherwise. See
# https://github.com/Kludex/python-multipart/pull/166 for details, but note
# that the implementation changed significantly in 0.0.14 via
# https://github.com/Kludex/python-multipart/pull/168.
#
# If *both* packages are installed, there are no file conflicts because the
# compatibility hack in this package is a directory (multipart/) and the other
# package is a single-file module (multipart.py). However, anything that uses
# this package via “import multipart” will be broken if the other package is
# installed, so we maintain the RPM conflict at least until all dependent
# packages have been adapted to use “import python_multipart”, and perhaps
# until upstream removes the compatibility hack in a future version.
Conflicts:      python3-multipart
# Ensure proper upgrade path from the old package
Obsoletes:      python3-multipart < 0.1

%description -n python3-python-multipart %{common_description}


%check -a
%pytest


%files -n python3-python-multipart -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
