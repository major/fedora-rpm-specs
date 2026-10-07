Name:           python-elevenlabs
Version:        2.71.0
Release:        %autorelease
Summary:        The official Python SDK for ElevenLabs

License:        MIT
URL:            https://github.com/elevenlabs/elevenlabs-python
Source:         %{pypi_source elevenlabs}

BuildSystem:    pyproject
BuildOption(install):  elevenlabs
BuildOption(generate_buildrequires): -x pyaudio

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%global _description %{expand:
The official Python SDK for ElevenLabs. ElevenLabs brings the most compelling,
rich and lifelike voices to creators and developers in just a few lines of
code.}

%description %_description

%package -n     python3-elevenlabs
Summary:        %{summary}

%description -n python3-elevenlabs %_description

%pyproject_extras_subpkg -n python3-elevenlabs pyaudio

%prep -a
%pyproject_patch_dependency pyaudio:drop_lower

%files -n python3-elevenlabs -f %{pyproject_files}


%changelog
%autochangelog
