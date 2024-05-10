%global uuid auto-power-profile@dmy3k.github.io

Name:          gnome-shell-extension-auto-power-profile
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       Gnome extension to automatically switch between power profiles based on power supply. 

Group:         User Interface/Desktops
License:       GPLv3
URL:           https://github.com/ublue-os/auto-power-profile
Source0:       %{url}/archive/refs/heads/main.tar.gz
BuildArch:     noarch

BuildRequires: make
BuildRequires: unzip
BuildRequires: gettext
BuildRequires: gnome-shell
BuildRequires: glib2

Requires:    gnome-shell >= 3.12
%description
Gnome extension to automatically switch between power profiles based on power supply.

%prep
%autosetup -n auto-power-profile-main

%install
gnome-extensions pack --extra-source=ui
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip ${uuid}.shell-extension.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
rm %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/schemas/gschemas.compiled
glib-compile-schemas %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/schemas/

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
