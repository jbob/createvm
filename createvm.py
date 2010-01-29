#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright (C) 2009, 2010 Markus Koch
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

def main():
  # Default values, empty means no default
  _suite = "jaunty"
  _arch = "i386"
  _mem = "512"
  _rootsize = "4096"
  _swapsize = "1024"
  _kernelflavour = "virtual"
  _hostname = ""
  _domain = "home"
  _mirror = "http://archive.ubuntu.com/ubuntu"
  _components = "main,universe"
  _addpkg = ["openssh-server", "acpid"]
  _user = ""
  _passw = ""
  _ip = "dhcp"
  _mask = "255.255.0.0"
  _net = "192.168.0.0"
  _bcast = "192.168.0.255"
  _gw = "192.168.0.1"
  _dns = "192.168.0.1"
  _bridge = "br0"
  _copy = ""


  # Get values from the user and build cmd
  cmd = "vmbuilder kvm ubuntu "

  suite = ""
  while suite == "":
    suite = raw_input("suite [%s]: " % _suite)
    if suite == "":
      suite = _suite
  cmd = cmd+"--suite '"+suite+"' "

  arch = ""
  while arch == "":
    arch = raw_input("arch [%s]: " % _arch)
    if arch == "":
      arch = _arch
  cmd = cmd+"--arch '"+arch+"' "

  mem = ""
  while mem == "":
    mem = raw_input("mem [%s]: " % _mem)
    if mem == "":
      mem = _mem
  cmd = cmd+"--mem '"+mem+"' "
    
  rootsize = ""
  while rootsize == "":
    rootsize = raw_input("rootsize [%s]: " % _rootsize)
    if rootsize == "":
      rootsize = _rootsize
  cmd = cmd+"--rootsize '"+rootsize+"' "

  swapsize = ""
  while swapsize == "":
    swapsize = raw_input("swapsize [%s]: " % _swapsize)
    if swapsize == "":
      swapsize = _swapsize
  cmd = cmd+"--swapsize '"+swapsize+"' "

  kernelflavour = ""
  while kernelflavour == "":
    kernelflavour = raw_input("kernel-flavour [%s]: " % _kernelflavour)
    if kernelflavour == "":
      kernelflavour = _kernelflavour
  cmd = cmd+"--kernel-flavour '"+kernelflavour+"' "

  hostname = ""
  while hostname == "":
    hostname = raw_input("hostname: ")
    if hostname == "":
      hostname = _hostname
  cmd = cmd+"--hostname '"+hostname+"' "

  domain = ""
  while domain == "":
    domain = raw_input("domain [%s]: " % _domain)
    if domain == "":
      domain = _domain
  cmd = cmd+"--domain '"+domain+"' "

  mirror = ""
  while mirror == "":
    mirror = raw_input("mirror [%s]: " % _mirror)
    if mirror == "":
      mirror = _mirror
  cmd = cmd+"--mirror '"+mirror+"' "

  components = ""
  while components == "":
    components = raw_input("components [%s]: " % _components)
    if components == "":
      components = _components
  cmd = cmd+"--components '"+components+"' "

  print("\nAdditional Packages:")
  print("Please specifiy one package per line. Depencies are installed"),
  print("automatically.")
  addpkg = "dummy"
  while addpkg != "":
    addpkg = raw_input("addppkg (return for none): ")
    if addpkg != "":
      _addpkg.append(addpkg)
  for package in _addpkg:
    cmd = cmd+"--addpkg '"+package+"' "
      
  user = ""
  while user == "":
    user = raw_input("user: ")
    if user == "":
      user = _user
  cmd = cmd+"--user '"+user+"' "

  passw = ""
  while passw == "":
    passw = raw_input("pass: ")
    if passw == "":
      passw = _passw
  cmd = cmd+"--pass '"+passw+"' "

  ip = ""
  while ip == "":
    ip = raw_input("ip [%s]: " % _ip)
    if ip == "":
      ip = _ip 
    if ip != "dhcp":
      cmd = cmd+"--ip '"+ip+"' "

      mask = ""
      while mask == "":
        mask = raw_input("mask [%s]: " % _mask)
        if mask == "":
          mask = _mask
      cmd = cmd+"--mask '"+mask+"' "

      net = ""
      while net == "":
        net = raw_input("net [%s]: " % _net)
        if net == "":
          net = _net
      cmd = cmd+"--net '"+net+"' "


      bcast = ""
      while bcast == "":
        bcast = raw_input("bcast [%s]: " % _bcast)
        if bcast == "":
          bcast = _bcast
      cmd = cmd+"--bcast '"+bcast+"' "

      gw = ""
      while gw == "":
        gw = raw_input("gw [%s]: " % _gw)
        if gw == "":
          gw = _gw
      cmd = cmd+"--gw '"+gw+"' "

      dns = ""
      while dns == "":
        dns = raw_input("dns [%s]: " % _dns)
        if dns == "":
          dns = _dns
      cmd = cmd+"--dns '"+dns+"' "

  bridge = ""
  while bridge == "":
    bridge = raw_input("bridge [%s]: " % _bridge)
    if bridge == "":
      bridge = _bridge
  cmd = cmd+"--bridge '"+bridge+"' "

  copy = raw_input("copy [%s]: " % _copy)
  if copy != "":
    cmd = cmd+"--copy '"+copy+"' "

  cmd = cmd+"--libvirt 'qemu:///system' ;"


  print "Resulting command:"
  print cmd
  answer = ""
  while answer == "":
    answer = raw_input("Do want to continue to create the VM? [y/n]: ")
    if answer=="y" or answer=="yes" or answer=="Y" or answer=="Yes" or answer=="Yes":
      os.system(cmd)

if __name__ == "__main__":
  main()
