/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * OpenerDialog1.java
 *
 * Created on Mar 16, 2012, 2:31:30 PM
 */

package com.nrims.managers;

import com.nrims.data.Opener;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

/**
 *
 * @author zkaufman
 */
public class OpenerManager extends javax.swing.JDialog implements ActionListener, ChangeListener {

   Opener op;
   boolean isOK = false;
   boolean forceOpen = false;
   int pixel_width, pixel_height, num_masses, num_planes, bits_per_pixel, file_size;
   long headersize, theoretical_filesize, actual_filesize;

    /** Creates new form OpenerDialog1 */
    public OpenerManager(java.awt.Frame parent, Opener opener) {
        super(parent);
        op = opener;
        initComponents();
        initComponentsCustom();
    }

    public void initComponentsCustom(){

       setTitle("ERROR: Bad Header Information");

       // Fill in the metadata.
       headersize = op.getHeaderSize();
       pixel_width = op.getWidth();
       pixel_height = op.getHeight();
       num_masses = op.getNMasses();
       num_planes = op.getNImages();
       bits_per_pixel = op.getBitsPerPixel();

       // Set the spinner values.
       spinner_headersize.setText(Long.toString(headersize));
       spinner_width.setValue(pixel_width);
       spinner_height.setValue(pixel_height);
       spinner_numMasses.setValue(num_masses);
       spinner_numPlanes.setValue(num_planes);
       if (bits_per_pixel == 2)
          jRadioButton_16bit.setSelected(true);
       else if (bits_per_pixel == 4)
          jRadioButton_32bit.setSelected(true);
       else if (bits_per_pixel == 8)
          jRadioButton_64bit.setSelected(true);

       // Set the spinner change listener.
       spinner_height.addChangeListener(this);
       spinner_numMasses.addChangeListener(this);
       spinner_numPlanes.addChangeListener(this);
       OK_button.addActionListener(this);
       Cancel_button.addActionListener(this);

       // Fill in actual file size.
       actual_filesize = op.getImageFile().length();
       jlabel_actual_filesize.setText(Long.toString(actual_filesize));

       calculateTheoreticalFilesize();

    }

    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
   // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
   private void initComponents() {

      spinner_height = new javax.swing.JSpinner();
      jLabel3 = new javax.swing.JLabel();
      spinner_width = new javax.swing.JSpinner();
      jLabel2 = new javax.swing.JLabel();
      spinner_numPlanes = new javax.swing.JSpinner();
      spinner_numMasses = new javax.swing.JSpinner();
      jLabel4 = new javax.swing.JLabel();
      jLabel7 = new javax.swing.JLabel();
      jLabel6 = new javax.swing.JLabel();
      jLabel5 = new javax.swing.JLabel();
      jlabel_actual_filesize = new javax.swing.JLabel();
      jLabel9 = new javax.swing.JLabel();
      jRadioButton_32bit = new javax.swing.JRadioButton();
      jRadioButton_16bit = new javax.swing.JRadioButton();
      jlabel_theoretical_filesize = new javax.swing.JLabel();
      jRadioButton_64bit = new javax.swing.JRadioButton();
      jLabel1 = new javax.swing.JLabel();
      jLabel12 = new javax.swing.JLabel();
      OK_button = new javax.swing.JButton();
      Cancel_button = new javax.swing.JButton();
      jLabel11 = new javax.swing.JLabel();
      spinner_headersize = new javax.swing.JTextField();
      forceCheckBox = new javax.swing.JCheckBox();

      setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);

      jLabel3.setText("number of masses:");

      jLabel2.setText("height (pixels):");

      jLabel4.setText("number of planes:");

      jLabel7.setText("bytes per pixel:");

      jLabel6.setText("Theoretical file size =");

      jLabel5.setText("header size:");

      jlabel_actual_filesize.setText("0");

      jLabel9.setText("Actual file size =");

      jRadioButton_32bit.setText("4 (32 bit image)");
      jRadioButton_32bit.addActionListener(new java.awt.event.ActionListener() {
         public void actionPerformed(java.awt.event.ActionEvent evt) {
            jRadioButton_32bitActionPerformed(evt);
         }
      });

      jRadioButton_16bit.setText("2 (16 bit image)");
      jRadioButton_16bit.addActionListener(new java.awt.event.ActionListener() {
         public void actionPerformed(java.awt.event.ActionEvent evt) {
            jRadioButton_16bitActionPerformed(evt);
         }
      });

      jlabel_theoretical_filesize.setText("0");

      jRadioButton_64bit.setText("8 (64 bit image)");
      jRadioButton_64bit.addActionListener(new java.awt.event.ActionListener() {
         public void actionPerformed(java.awt.event.ActionEvent evt) {
            jRadioButton_64bitActionPerformed(evt);
         }
      });

      jLabel1.setText("width (pixels):");

      jLabel12.setText("bits");

      OK_button.setText("OK");
      OK_button.addActionListener(new java.awt.event.ActionListener() {
         public void actionPerformed(java.awt.event.ActionEvent evt) {
            OK_buttonActionPerformed(evt);
         }
      });

      Cancel_button.setText("Cancel");

      jLabel11.setText("bits");

      spinner_headersize.setEditable(false);
      spinner_headersize.setText("0");
      spinner_headersize.addActionListener(new java.awt.event.ActionListener() {
         public void actionPerformed(java.awt.event.ActionEvent evt) {
            spinner_headersizeActionPerformed(evt);
         }
      });

      forceCheckBox.setText("force open");
      forceCheckBox.addActionListener(new java.awt.event.ActionListener() {
         public void actionPerformed(java.awt.event.ActionEvent evt) {
            forceCheckBoxActionPerformed(evt);
         }
      });

      javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
      getContentPane().setLayout(layout);
      layout.setHorizontalGroup(
         layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGroup(layout.createSequentialGroup()
            .addContainerGap()
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
               .addGroup(layout.createSequentialGroup()
                  .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                     .addComponent(jLabel2)
                     .addComponent(jLabel1)
                     .addComponent(jLabel5)
                     .addComponent(jLabel3)
                     .addComponent(jLabel4)
                     .addComponent(jLabel7))
                  .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                  .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                     .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                        .addComponent(spinner_numPlanes)
                        .addComponent(spinner_width, javax.swing.GroupLayout.DEFAULT_SIZE, 49, Short.MAX_VALUE)
                        .addComponent(spinner_height)
                        .addComponent(spinner_numMasses))
                     .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                        .addGroup(layout.createSequentialGroup()
                           .addComponent(Cancel_button)
                           .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                           .addComponent(OK_button))
                        .addGroup(layout.createSequentialGroup()
                           .addComponent(jRadioButton_16bit)
                           .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                           .addComponent(jRadioButton_32bit))
                        .addComponent(forceCheckBox))
                     .addComponent(jRadioButton_64bit)
                     .addComponent(spinner_headersize, javax.swing.GroupLayout.PREFERRED_SIZE, 107, javax.swing.GroupLayout.PREFERRED_SIZE)))
               .addGroup(layout.createSequentialGroup()
                  .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                     .addComponent(jLabel9)
                     .addComponent(jLabel6))
                  .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                  .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                     .addGroup(layout.createSequentialGroup()
                        .addComponent(jlabel_actual_filesize)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel12))
                     .addGroup(layout.createSequentialGroup()
                        .addComponent(jlabel_theoretical_filesize)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel11)))))
            .addContainerGap(22, Short.MAX_VALUE))
      );
      layout.setVerticalGroup(
         layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
         .addGroup(layout.createSequentialGroup()
            .addContainerGap()
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(jLabel5)
               .addComponent(spinner_headersize, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
            .addGap(18, 18, 18)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(spinner_width, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
               .addComponent(jLabel1))
            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(spinner_height, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
               .addComponent(jLabel2))
            .addGap(18, 18, 18)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(jLabel3)
               .addComponent(spinner_numMasses, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
            .addGap(18, 18, 18)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(jLabel4)
               .addComponent(spinner_numPlanes, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
            .addGap(18, 18, 18)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(jLabel7)
               .addComponent(jRadioButton_16bit)
               .addComponent(jRadioButton_32bit))
            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
            .addComponent(jRadioButton_64bit)
            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(jlabel_theoretical_filesize)
               .addComponent(jLabel11)
               .addComponent(jLabel6))
            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(jlabel_actual_filesize)
               .addComponent(jLabel12)
               .addComponent(jLabel9)
               .addComponent(forceCheckBox))
            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 51, Short.MAX_VALUE)
            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
               .addComponent(OK_button)
               .addComponent(Cancel_button))
            .addContainerGap())
      );

      pack();
   }// </editor-fold>//GEN-END:initComponents

    private void jRadioButton_32bitActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jRadioButton_32bitActionPerformed
       jRadioButton_16bit.setSelected(false);
       jRadioButton_64bit.setSelected(false);
       jRadioButton_32bit.setSelected(true);
       bits_per_pixel = 4;
       calculateTheoreticalFilesize();
}//GEN-LAST:event_jRadioButton_32bitActionPerformed

    private void jRadioButton_16bitActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jRadioButton_16bitActionPerformed
       jRadioButton_32bit.setSelected(false);
       jRadioButton_64bit.setSelected(false);
       jRadioButton_16bit.setSelected(true);
       bits_per_pixel = 2;
       calculateTheoreticalFilesize();
}//GEN-LAST:event_jRadioButton_16bitActionPerformed

    private void jRadioButton_64bitActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jRadioButton_64bitActionPerformed
       jRadioButton_16bit.setSelected(false);
       jRadioButton_32bit.setSelected(false);
       jRadioButton_64bit.setSelected(true);
       bits_per_pixel = 8;
       calculateTheoreticalFilesize();
}//GEN-LAST:event_jRadioButton_64bitActionPerformed

    private void OK_buttonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_OK_buttonActionPerformed
       // TODO add your handling code here:
}//GEN-LAST:event_OK_buttonActionPerformed

    private void spinner_headersizeActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_spinner_headersizeActionPerformed
       // TODO add your handling code here:
    }//GEN-LAST:event_spinner_headersizeActionPerformed

    private void forceCheckBoxActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_forceCheckBoxActionPerformed
       forceOpen = forceCheckBox.isSelected();
       calculateTheoreticalFilesize();
    }//GEN-LAST:event_forceCheckBoxActionPerformed

   // Variables declaration - do not modify//GEN-BEGIN:variables
   private javax.swing.JButton Cancel_button;
   private javax.swing.JButton OK_button;
   private javax.swing.JCheckBox forceCheckBox;
   private javax.swing.JLabel jLabel1;
   private javax.swing.JLabel jLabel11;
   private javax.swing.JLabel jLabel12;
   private javax.swing.JLabel jLabel2;
   private javax.swing.JLabel jLabel3;
   private javax.swing.JLabel jLabel4;
   private javax.swing.JLabel jLabel5;
   private javax.swing.JLabel jLabel6;
   private javax.swing.JLabel jLabel7;
   private javax.swing.JLabel jLabel9;
   private javax.swing.JRadioButton jRadioButton_16bit;
   private javax.swing.JRadioButton jRadioButton_32bit;
   private javax.swing.JRadioButton jRadioButton_64bit;
   private javax.swing.JLabel jlabel_actual_filesize;
   private javax.swing.JLabel jlabel_theoretical_filesize;
   private javax.swing.JTextField spinner_headersize;
   private javax.swing.JSpinner spinner_height;
   private javax.swing.JSpinner spinner_numMasses;
   private javax.swing.JSpinner spinner_numPlanes;
   private javax.swing.JSpinner spinner_width;
   // End of variables declaration//GEN-END:variables

   public void actionPerformed(ActionEvent e) {
      if (e.getActionCommand().matches("OK")) {
         op.setWidth(pixel_width);
         op.setHeight(pixel_height);
         op.setNMasses(num_masses);
         op.setNImages(num_planes);
         if (jRadioButton_16bit.isSelected())
            op.setBitsPerPixel((short)2);
         else if (jRadioButton_32bit.isSelected())
            op.setBitsPerPixel((short)4);
         else if (jRadioButton_64bit.isSelected())
            op.setBitsPerPixel((short)8);
         isOK = true;
      } else if (e.getActionCommand().matches("Cancel")) {
         isOK = false;
      }
      dispose();
   }

   public void stateChanged(ChangeEvent e) {
      pixel_width = (Integer)spinner_width.getValue();
      pixel_height = (Integer)spinner_height.getValue();
      num_masses = (Integer)spinner_numMasses.getValue();
      num_planes = (Integer)spinner_numPlanes.getValue();
      calculateTheoreticalFilesize();
   }

   private void calculateTheoreticalFilesize() {
      theoretical_filesize = ((long)pixel_width*(long)pixel_height*(long)num_masses*(long)num_planes*(long)bits_per_pixel) + (long)headersize;
      jlabel_theoretical_filesize.setText(Long.toString(theoretical_filesize));
      if (forceCheckBox.isSelected())
         OK_button.setEnabled(true);
      else {
         if (theoretical_filesize <= actual_filesize)
            OK_button.setEnabled(true);
         else
            OK_button.setEnabled(false);
      }
   }

   public boolean isOK() {
      return isOK;
   }

   public boolean forceOpen() {
      return forceOpen;
   }

}
