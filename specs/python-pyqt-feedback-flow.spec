Name:           python-pyqt-feedback-flow
Version:        0.3.6
Release:        %autorelease
Summary:        Show feedback in toast-like notifications

# The entire source is MIT, except for the contents of icons/, which are
# content and are licensed CC-BY-SA-4.0. These files would be used for certain
# documentation and examples; they do not contribute to the binary RPMs.
License:        MIT
SourceLicense:  %{license} AND CC-BY-SA-4.0
URL:            https://github.com/firefly-cpp/pyqt-feedback-flow
Source:         %{url}/archive/%{version}/pyqt-feedback-flow-%{version}.tar.gz

BuildArch:      noarch

BuildSystem:    pyproject
BuildOption(install): --assert-license pyqt_feedback_flow

# Test deps.: see [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-qt}

%global common_description %{expand:
On many occasions, notifications can be a valuable tool to inform a user about
specific events. Sometimes, static notifications or pop-up windows may provide
adequate feedback; however, there are some cases where flowing notifications
can be more appropriate.

This software allows us to show flowing notifications in the realm of a text or
a picture. Both text and pictures (raster and vector) can be customized
according to the user’s wishes, which offers a wide variety of possibilities
for providing flowing feedback.}

%description %{common_description}


%package -n python3-pyqt-feedback-flow
Summary:        %{summary}

# The python3dist(pyqt6) dependency generated from PyQt6 in pyproject.toml is
# satisfied by python3-pyqt6-base, but this project uses PyQt6.QtSvg, which is
# packaged along with other “non-core” modules in python3-pyqt6. Since this is
# not represented (and currently cannot be represented) in the Python metadata,
# we need explicit BuildRequires *and* Requires on the full python3-pyqt6.
BuildRequires:  python3-pyqt6
Requires:       python3-pyqt6

%description -n python3-pyqt-feedback-flow %{common_description}


%check -a
%pytest --verbose


%files -n python3-pyqt-feedback-flow -f %{pyproject_files}
%doc CITATION.cff
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
